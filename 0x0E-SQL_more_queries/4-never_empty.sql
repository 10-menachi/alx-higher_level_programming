-- This script creates the table id_not_null on your MySQL server.
CREATE TABLE IF NOT EXISTS id_not_null(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256),
    PRIMARY KEY (id)
);