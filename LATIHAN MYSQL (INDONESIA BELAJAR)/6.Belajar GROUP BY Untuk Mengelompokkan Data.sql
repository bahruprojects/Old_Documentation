-- Belajar GROUP BY Untuk Mengelompokkan Data

SHOW databases;
USE classicmodels;
SHOW tables;

DESCRIBE orders;

SELECT status, count(*) 
FROM orders
WHERE status = 'resolved';

SELECT status, count(*)
FROM orders
GROUP BY status;

SELECT status, ordernumber
FROM orders
WHERE status = 'Cancelled';

SELECT (quantityOrdered*priceeach) revenue
FROM orderdetails;

SELECT o.status, sum(quantityOrdered*priceeach) total_revenue
FROM orders o INNER JOIN orderdetails od USING (ordernumber)
GROUP BY o.status;


