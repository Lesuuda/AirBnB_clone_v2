-- Create or use the database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create or update the user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant privileges
GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost' WITH GRANT OPTION;
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

