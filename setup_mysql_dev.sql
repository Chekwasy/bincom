-- prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS bincomphptest;
CREATE USER IF NOT EXISTS 'chekwasy_dev'@'localhost' IDENTIFIED BY 'CHEKWASY_dev_pwd_001';
GRANT ALL PRIVILEGES ON `bincomphptest`.* TO 'chekwasy_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'chekwasy_dev'@'localhost';
FLUSH PRIVILEGES;
