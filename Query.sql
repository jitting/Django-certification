CREATE FUNCTION trigger_function()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
UPDATE Book
SET quantityonhand = quantityonhand - NEW.quantity
WHERE Bookcode = NEW.Bookcode

