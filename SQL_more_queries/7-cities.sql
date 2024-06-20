-- 7.Cities table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT UNIQUE PRIMARY KEY,
    state_id INT,
    name VARCHAR(256),
    FOREIGN KEY (state_id) REFERENCES states(id)
);
