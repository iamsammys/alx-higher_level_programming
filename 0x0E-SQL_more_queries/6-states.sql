-- Create database and table
-- DDL to create a database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Switch to database
USE hbtn_0d_usa;
-- DDL query to create a table states
CREATE TABLE IF NOT EXISTS states (
	id INT AUTO_INCREMENT UNIQUE,
	name VARCHAR (256) NOT NULL
);
