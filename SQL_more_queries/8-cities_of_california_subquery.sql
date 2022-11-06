-- List all records under constraints in table
SELECT id, name FROM cities WHERE id IN (SELECT id FROM states WHERE name = 'California'); 