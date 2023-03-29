-- Exercise 1 import bus.sql
SHOW databases;
USE bus;

-- Exercise 2: How are the tables in the databases related?
SHOW CREATE TABLE bus;
SHOW CREATE TABLE driver;

-- Exercise 3: Add the following drivers. What happens and why?
-- Mary's INSERT INTO fails because the licence number is a primary key and cannot be null
INSERT INTO driver VALUES (NULL, "Mary", NULL);
INSERT INTO driver VALUES ("FF88345", "Sean", "191-G-123");
INSERT INTO driver(licenceNo,name,busReg) VALUES ("RR2423", "Bob", NULL);

-- Exercise 4: Add the following buses. What happens and why?
-- the INSERT INTO for the Diesel vehicle fails as that registration is already in the primary key reg column
-- the INSERT INTO for the Ethanol vehicle fails as that column is restricted to pre-defined values Diesel, Petrol or Electric
INSERT INTO bus VALUES("12-G-1323", 34, "Diesel");
INSERT INTO bus VALUES("171-G-885", 84, "Petrol");
INSERT INTO bus VALUES("191-D-45890", 120, "Ethanol");

-- Exercise 5: Update driver’s licences that contain the letters “F” or “R” to have the letters “T-“ before their current licence number.
SELECT * FROM driver;
SELECT * FROM bus;
UPDATE driver
SET licenceNo = CONCAT(IF(licenceNo="%F%", "T-",NULL),licenceNo);

-- Exercise 6: Delete driver Alan. What happens and why?
-- operation halted as mySQL is running in safe mode, where deletions must refer to the primary key of a table
DELETE FROM driver
WHERE name = "Alan";

-- Exercise 7: Delete bus 161-D-1323. What happens and why?
-- operation works regardless of safe mode as WHERE clause references the key
DELETE FROM bus
WHERE reg = "161-D-1323";

-- Exercise 8: import bus2.sql
SHOW databases;
USE bus2;

-- Exercise 9: Delete bus 161-D-1323. What happens and why?
-- operation works regardless of safe mode as WHERE clause references the key
DELETE FROM bus
WHERE reg = "161-D-1323";

-- Exercise 10: import employees2.sql
SHOW databases;
USE employees2;

-- Exercise 11: Show the emp_no, first_name and last_name of employees born in the average year. The average year should be rounded down to the 
-- nearest whole number. For example, 1949.1 becomes 1949; 1949.9 becomes 1949; 1949.0 becomes 1949.
SELECT emp_no, first_name, last_name, YEAR(birth_date) AS birth_year FROM employees;

-- Exercise 12: Show the emp_no, first_name, last_name and name of the department each employee is in.
SELECT DISTINCT e.emp_no, e.first_name, e.last_name, d.name FROM employees AS e
INNER JOIN salaries AS s ON e.emp_no = s.emp_no
INNER JOIN dept AS d ON s.dept_no = d.dept_no;
