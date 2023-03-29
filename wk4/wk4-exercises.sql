-- Exercise 1: import garage database
SHOW databases;

USE garage;

-- Exercise 2: how are the tables related? One-to-many relationship on manu_code columns
-- below will display schematic information as the DESCRIBE command would, but with any keys and relationships included
SHOW CREATE TABLE manufacturer;

-- Exercise 3: Show the manu_code, manu_name and the first 10 characters of the manu_details followed by three dots (…) for each manufacturer
SELECT manu_code, manu_name, CONCAT(LEFT(manu_details, 10),"...") FROM manufacturer;

-- Exercise 4: Show the average length of the manu_name (displayed as “Length”) with 0 characters after the decimal point
SELECT FORMAT(AVG(LENGTH(manu_name)),'N0') AS Length FROM manufacturer;

-- Exercise 5: Show all details of all vehicles plus an extra column called “cost” which has the value 1.45 if the fuel is petrol otherwise has the value 1.30.
SELECT *, CASE WHEN fuel="petrol" THEN 1.45 ELSE 1.30 END AS cost FROM vehicle;

-- Exercise 6: Show all the reg, manu_code and associated manu_name for each vehicle
SELECT v.reg, m.manu_code, m.manu_name FROM  manufacturer AS m
INNER JOIN vehicle AS v ON m.manu_code = v.manu_code;

-- Exercise 7: Show the manu_code and manu_name as well as associated reg, for each manufacturer who has vehicles listed in the vehicle table.
SELECT * FROM  manufacturer AS m
INNER JOIN vehicle AS v ON m.manu_code = v.manu_code;

-- Exercise 8: Show the manu_code and manu_name as well as associated reg, for all manufacturers and if they have vehicles listed in the vehicle table, show the reg of it.
SELECT * FROM manufacturer AS m
LEFT JOIN vehicle AS v ON m.manu_code = v.manu_code;

-- Exercise 9: Write a stored procedure called price_less_than that takes one parameter of type decimal(8,2) which represents the price of a vehicle:
-- price_less_than(p decimal(8,2)). The procedure should then return the following details for all vehicles where the price of the vehicle is less 
-- than p sorted by ascending price: Reg, Manu_code, Manu_name, Mileage, Price
CALL price_less_than2(10000.00);