show databases;

use employees;

-- Exercise 4
SELECT *, CONCAT(LEFT(first_name,1), LEFT(last_name,1)) AS initials 
FROM employees;

-- Exercise 5
SELECT *, MONTH(hire_date) AS month 
FROM employees
WHERE gender="F"
AND YEAR(birth_date) > "1949"
AND YEAR(birth_date) < "1960"
AND hire_date BETWEEN "1987-08-31" AND "1991-02-28"
ORDER BY hire_date;

-- Exercise 6
SELECT *, FORMAT(salary,"F2") AS salary
FROM salaries;

-- Exercise 7
SELECT e.emp_no, ROUND(AVG(s.salary),2) AS avg_sal
FROM employees as e
INNER JOIN salaries AS s ON s.emp_no = e.emp_no
GROUP BY e.emp_no;

-- Exercise 8
SELECT e.emp_no, ROUND(MAX(s.salary),2) AS max_sal
FROM employees as e
INNER JOIN salaries AS s ON s.emp_no = e.emp_no
GROUP BY e.emp_no;

-- Exercise 9
SELECT e.emp_no, ROUND(AVG(s.salary),2) AS avg_sal
FROM employees as e
INNER JOIN salaries AS s ON s.emp_no = e.emp_no
WHERE s.salary > 80000
AND e.emp_no IN (10001, 10021,10033,10087)
GROUP BY e.emp_no;

-- Exercise 10
SELECT e.emp_no, ROUND(AVG(s.salary),0) AS avg_sal
FROM employees as e
INNER JOIN salaries AS s ON s.emp_no = e.emp_no
WHERE s.salary > 90000
GROUP BY e.emp_no;

-- Exercise 11
SELECT emp_no, CASE WHEN gender="M" THEN "Mr." ELSE "Ms." END AS title, first_name, last_name, gender 
FROM employees
ORDER BY emp_no
LIMIT 15;

-- Exercise 12
SELECT
	e.emp_no,
    MAX(s.salary) AS max_sal,
    CASE
		WHEN MAX(s.salary)<40000 THEN "30%"
        WHEN MAX(s.salary)<60000 THEN "40%"
        WHEN MAX(s.salary)<80000 THEN "50%"
        ELSE "60%"
	END AS tax
FROM employees as e
INNER JOIN salaries AS s ON s.emp_no = e.emp_no
GROUP BY e.emp_no;

-- Exercise 13
SELECT *, CASE WHEN DATEDIFF(to_date, from_date) < 365 THEN "Under 1 Year" ELSE "Over 1 Year" END AS time FROM salaries ORDER BY emp_no;

-- Exercise 14
SELECT *, ROUND(DATEDIFF(hire_date, birth_date)/365, 1) AS age FROM employees;

-- Exercise 15
CALL mon_yr(1985);

-- Exercise 16
CALL mon_yr(1985,NULL);