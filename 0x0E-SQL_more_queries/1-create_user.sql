-- A script that lists all privileges of user_0d_1 and user_0d_2
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY "user_0d_1_pwd";
-- Grant privileges
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@localhost;
