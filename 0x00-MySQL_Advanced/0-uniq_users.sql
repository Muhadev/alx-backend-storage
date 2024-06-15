-- Task 0: We are all unique!

-- Check if the `users` table exists before attempting to create it
-- If the table exists, this script should not fail and should not attempt to recreate the table.

-- Connect to the `holberton` database
USE holberton;

-- Create the `users` table if it does not already exist
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Attribute id is an integer, never null, auto increment and primary key
    email VARCHAR(255) NOT NULL UNIQUE, -- Attribute email is a string (255 characters), never null and unique
    name VARCHAR(255) -- Attribute name is a string (255 characters)
);

-- Script completed successfully
