CREATE DATABASE if not exists calculator_data;
USE calculator_data;
CREATE TABLE if not exists add_data ( user_ip VARCHAR(100), times INT, sum FLOAT, PRIMARY KEY (user_ip) );