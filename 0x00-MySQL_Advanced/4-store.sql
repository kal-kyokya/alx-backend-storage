-- Create a trigger updating a table
-- for each access made to it

CREATE TRIGGER UpdateItems
AFTER INSERT
ON orders
FOR EACH ROW
	UPDATE items
	SET quantity = quantity - NEW.number
	WHERE name = NEW.item_name;
