-- Create a table named 'users'

-- Ensures the table does not already exist
-- before proceeding with its creation

CREATE TABLE IF NOT EXISTS users (
       id INT NOT NULL AUTO_INCREMENT UNIQUE,
       email VARCHAR(255) NOT NULL UNIQUE,
       name VARCHAR(255),
       country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
