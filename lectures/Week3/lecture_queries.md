# Queries ran during lecture

Carriers table:
```sql
SELECT * FROM carriers; -- Grab all information from the carriers table
SELECT name, year_founded FROM carriers;

SELECT * FROM carriers WHERE id = 2; -- Ideal way
SELECT * FROM carriers WHERE name = 'Delta'; -- Another way to grab Delta - but be careful of duplicate values!
SELECT * FROM carriers WHERE year_founded > 1960; -- Adding a condition to a query

UPDATE carriers SET year_founded = 1932, name = "Alaska" WHERE id = 1;

DELETE FROM carriers WHERE id = 3;

-- A multi-line query:
INSERT INTO carriers (name, hq_city, year_founded, total_workers) 
VALUES ("Southwest", "Dallas", 1967, 20000), ("United", "Chicago", 1955, 40000);

-- Joining tables (JOIN vs. LEFT JOIN)
SELECT * FROM carriers JOIN flights ON carriers.id = flights.carrier_id;
SELECT * FROM carriers LEFT JOIN flights ON carriers.id = flights.carrier_id;
SELECT * FROM carriers LEFT JOIN flights ON carriers.id = flights.carrier_id wHERE carriers.id = 2;
```

Flights table:
```sql
INSERT INTO flights (number, starting_city, ending_city, carrier_id) VALUES (344, "Seattle", "San Diego", 1);

SELECT * FROM flights JOIN carriers ON flights.carrier_id = carriers.id; -- LEFT JOIN not needed here
```
