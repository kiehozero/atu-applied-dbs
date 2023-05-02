CREATE DEFINER=`root`@`localhost` PROCEDURE `price_less_than2`(p decimal(8,2))
    DETERMINISTIC
BEGIN
	SELECT v.reg, v.manu_code, m.manu_name, v.mileage, v.price 
    FROM vehicle as v
    INNER JOIN manufacturer AS m ON v.manu_code = m.manu_code
    WHERE v.price < p
    ORDER BY v.price ASC;
END