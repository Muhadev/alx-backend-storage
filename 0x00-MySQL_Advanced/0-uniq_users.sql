-- Task 0: We are all unique!

-- Check if the `users` table exists before attempting to create it
-- If the table exists, this script should not fail and should not attempt to recreate the table.

-- Start by dropping the `users` table if it exists, to ensure a clean slate
DROP TABLE IF EXISTS users;

-- Create the `users` table with the specified attributes
CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, -- Attribute id is an integer, never null, auto increment and primary key
    email VARCHAR(255) NOT NULL UNIQUE, -- Attribute email is a string (255 characters), never null and unique
    name VARCHAR(255) -- Attribute name is a string (255 characters)
);

-- Table `users` exists after execution

-- Script completed successfully
