-- Create the 'auth' user for all hosts ('%') and set the password
CREATE USER 'auth'@'%' IDENTIFIED BY 'Aauth123';

-- Create the database
CREATE DATABASE auth;

-- Grant privileges to the 'auth' user on the 'auth' database for all hosts ('%')
GRANT ALL PRIVILEGES ON auth.* TO 'auth'@'%';

-- Select the database to use
USE auth;

-- Create the 'users' table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Insert a sample user into the 'users' table
INSERT INTO users (username, password) VALUES ('choudharyu2003@gmail.com', 'admin');
