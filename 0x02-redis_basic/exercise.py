#!/usr/bin/env python3
"""
Redis caching module.
"""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps

def count_calls(method: Callable) -> Callable:
    """
    Decorator to count calls to a method.

    Args:
        method: The method to be decorated.

    Returns:
        Callable: The wrapped method with call count functionality.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Union[str, bytes, int, float, None]:
        """
        Wrapper function to increment the call count and call the original method.

        Args:
            self: The instance of the class.
            *args: Positional arguments for the method.
            **kwargs: Keyword arguments for the method.

        Returns:
            The result of the original method.
        """
        # Increment the call count in Redis
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return wrapper

class Cache:
    """
    Cache class utilizing Redis for storage.
    """

    def __init__(self) -> None:
        """
        Initialize Redis connection and flush the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis under a randomly generated key.

        Args:
            data: Data to store in Redis. Can be str, bytes, int, or float.

        Returns:
            str: Randomly generated key under which the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable[[bytes], Union[str, int, float]]] = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis and optionally apply a conversion function.

        Args:
            key: Key string to look up in Redis.
            fn: Optional callable to apply to the retrieved data.

        Returns:
            Retrieved data in its original type, or transformed by fn if provided.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a string from Redis.

        Args:
            key: Key string to look up in Redis.

        Returns:
            str: The retrieved string, or None if the key does not exist.
        """
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer from Redis.

        Args:
            key: Key string to look up in Redis.

        Returns:
            int: The retrieved integer, or None if the key does not exist.
        """
        return self.get(key, fn=int)