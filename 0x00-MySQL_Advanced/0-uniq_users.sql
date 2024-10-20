-- Create a table named 'users'

-- Ensure the table does not already exist
-- before attempting table creation

IF NOT EXISTS CREATE TABLE users (
   id INT PRIMARY KEY,
   email VARCHAR(255) UNIQUE NOT NULL,
   name VARCHAR(255)
)
