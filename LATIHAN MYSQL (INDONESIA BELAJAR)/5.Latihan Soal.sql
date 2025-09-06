# SOAL 4
USE classicmodels;
SELECT o.ordernumber, c.customernumber, c.customername
FROM orders o
INNER JOIN orderdetails od USING (ordernumber) INNER JOIN products p USING (productcode)
INNER JOIN customers c 
ORDER BY o.ordernumber