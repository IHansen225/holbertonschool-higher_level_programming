-- Create a database and a table under certain conditions
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE AUTOINCREMENT NOT NULL, name VARCHAR(256) NOT NULL, PRIMARY KEY (id));