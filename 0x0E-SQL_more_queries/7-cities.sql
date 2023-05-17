-- Create database and table
-- DDL create table hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Switch to database
USE hbtn_0d_usa;
-- Create table cities
CREATE TABLE IF NOT EXISTS cities (
	id INT AUTO_INCREMENT UNIQUE PRIMARY KEY NOT NULL,
	state_id INT NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states (id),
	name VARCHAR (256) NOT NULL
	);
