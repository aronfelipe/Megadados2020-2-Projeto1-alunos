DROP TABLE IF EXISTS tasks;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    uuid BINARY(255) PRIMARY KEY,
    name NVARCHAR(1024)
);

CREATE TABLE tasks (
    uuid BINARY(255) PRIMARY KEY,
    description NVARCHAR(1024),
    completed BOOLEAN,
    user_uuid BINARY(255) NULL,
    CONSTRAINT foreign_key_user
    FOREIGN KEY (user_uuid)
    REFERENCES users(uuid)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

-- DROP TABLE IF EXISTS tasks;
-- DROP TABLE IF EXISTS users;

-- CREATE TABLE users(
--     username NVARCHAR(20) PRIMARY KEY 
-- );

-- CREATE TABLE tasks (
--     uuid BINARY(16) PRIMARY KEY,
--     description NVARCHAR(1024),
--     completed BOOLEAN,
--     username NVARCHAR(20),
--     CONSTRAINT fk_user
--     FOREIGN KEY (username)
--     REFERENCES users (username)
--     ON UPDATE CASCADE
--     ON DELETE CASCADE
-- );