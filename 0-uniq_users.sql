-- Task 0: We are all unique!

-- This script creates a table `users` with specified attributes:
-- - id: integer, auto increment, primary key
-- - email: string (255), unique, not null
-- - name: string (255)

-- If the table already exists, it will not fail.

USE holberton;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
