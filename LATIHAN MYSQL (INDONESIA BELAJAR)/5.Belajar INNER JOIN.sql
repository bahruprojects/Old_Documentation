-- Belajar INNER JOIN 

SHOW databases;
USE classicmodels;
SHOW tables;
DESCRIBE productlines;
SELECT * FROM productlines;

SELECT * FROM products;

-- INNER JOIN (Cara 1)
SELECT t1.productCode, t1.productName, t2.textDescription
FROM products t1 INNER JOIN productlines t2
ON  t1.productline = t2.productline;

-- INNER JOIN (Cara 2)
SELECT t1.productCode, t1.productName, t2.textDescription
FROM products t1 INNER JOIN productlines t2
USING  (productline);

SELECT t1.productCode, t1.productName, t1.buyprice, t2.textDescription
FROM products t1 INNER JOIN productlines t2
USING  (productline)
WHERE t1.buyprice > 100;

SELECT o.ordernumber, o.orderdate, p.productname, od.quantityOrdered, od.priceEach
FROM orders o INNER JOIN orderdetails od USING (ordernumber)
INNER JOIN products p USING (productcode)
ORDER BY o.ordernumber;


SELECT o.ordernumber, o.orderdate, p.productname, od.quantityOrdered, od.priceEach
FROM orders o INNER JOIN orderdetails od USING (ordernumber)
INNER JOIN products p USING (productcode)
WHERE orderNumber = 10200
ORDER BY o.ordernumber;
