#!/usr/bin/env python3
"""
Redis caching module.
"""

import redis
import uuid
from typing import Union

class Cache:
    """
    Cache class utilizing Redis for storage.
    """

    def __init__(self):
        """
        Initialize Redis connection and flush the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

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