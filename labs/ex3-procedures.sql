CREATE DEFINER=`root`@`localhost` PROCEDURE `mon_yr`(y INTEGER, m INTEGER)
    DETERMINISTIC
BEGIN
	IF m IS NULL THEN
		SELECT *
		FROM employees
		WHERE YEAR(hire_date)=y;
	ELSE
	-- Exercise 15 was this part only
		SELECT *
		FROM employees
		WHERE YEAR(hire_date)=y AND MONTH(hire_date)=m;
	END IF;
END