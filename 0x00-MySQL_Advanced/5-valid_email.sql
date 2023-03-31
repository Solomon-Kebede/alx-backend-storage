-- Write a SQL script that creates a trigger that resets the attribute `valid_email` only when the `email` has been changed.

-- **Context**: *`Nothing related to MySQL, but perfect for user email validation - distribute the logic to the database itself!*

-- DELIMETER //
-- CREATE TRIGGER reset_valid_email
-- BEFORE UPDATE ON `user`
-- FOR EACH ROW 
-- BEGIN
--   IF NEW.email != OLD.email THEN
--     SET NEW.valid_email = false;
--   END IF;
-- END //
-- DELIMETER ;


-- https://dev.mysql.com/doc/refman/5.7/en/trigger-syntax.html

DELIMITER //

CREATE TRIGGER reset_email
BEFORE UPDATE ON `users` FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email THEN
        SET NEW.valid_email = 0;
    END IF;

END //

DELIMITER ;