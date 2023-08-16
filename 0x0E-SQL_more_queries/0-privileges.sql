-- This script lists all privileges granted to given users.
-- connect to the database.
mysql -u root -p
SHOW GRANTS FOR 'user_0d_1'@'localhost';
-- List privileges for another user.
SHOW GRANTS FOR 'user_0d_2'@'localhost';