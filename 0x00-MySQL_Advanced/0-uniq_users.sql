-- Create a table named 'users'

-- Ensure the table does not already exist
-- before attempting table creation

CREATE TABLE IF NOT EXISTS users (
   id INT AUTO_INCREMENT PRIMARY KEY,
   email VARCHAR(255) UNIQUE NOT NULL,
   name VARCHAR(255)
);
