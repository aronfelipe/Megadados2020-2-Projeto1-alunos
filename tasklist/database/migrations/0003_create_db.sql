-- ALTER TABLE tasks
--     ADD user_uuid BINARY(16);

-- ALTER TABLE tasks
--     CONSTRAINT foreign_key_user ADD FOREIGN KEY (user_uuid) REFERENCES users(uuid) ON DELETE CASCADE;