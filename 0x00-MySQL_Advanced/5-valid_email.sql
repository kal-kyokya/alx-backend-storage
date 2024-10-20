-- Create a trigger that permits updation
-- only upon fulfillment of condition

DELIMITER $$
CREATE TRIGGER reset
BEFORE UPDATE
ON users
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
	SET NEW.valid_email = 0;
    END IF;
END $$

DELIMITER;
