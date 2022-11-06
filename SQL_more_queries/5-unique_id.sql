-- Create a non null unique PK table
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT(1) UNIQUE NOT NULL, name VARCHAR(256) NOT NULL);