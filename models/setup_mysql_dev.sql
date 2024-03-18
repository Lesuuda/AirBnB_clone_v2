-- creates a database if it does not exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- creates a user if it does not exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- grants all permissions on hbnb_dev_db to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db . * TO 'hbnb_dev'@'localhost';
-- grants select permissions on performance_schema to hbnb_dev
GRANT SELECT ON performance_schema TO . * 'hbnb_dev'@'localhost';