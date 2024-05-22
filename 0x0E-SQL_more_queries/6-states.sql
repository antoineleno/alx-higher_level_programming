-- Creates the database hbtn_0d_usa and table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT AUTO INCREMENT UNIQUE NOT NULL, name VARCHAR(256), PRIMARY KEY(id));

