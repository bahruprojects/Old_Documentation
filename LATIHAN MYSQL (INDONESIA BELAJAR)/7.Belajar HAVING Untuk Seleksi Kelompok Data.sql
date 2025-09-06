-- Belajar HAVING Untuk Seleksi Kelompok Data

SHOW databases; 
USE classicmodels; 
SHOW tables;

SELECT  ordernumber, sum(quantityordered) items_count,
sum(priceeach*quantityordered) total_revenue
FROM orderdetails
GROUP BY ordernumber
HAVING total_revenue > 1000
AND items_count > 600;

SELECT ordernumber, sum(quantityordered) items_count,
sum(quantityordered * priceeach) total_revenue
FROM orderdetails
WHERE priceeach > 100
GROUP BY ordernumber
HAVING total_revenue > 1000 
AND items_count > 100;


SELECT o.status, sum(od.priceeach * od.quantityordered) total_revenue
FROM orders o INNER JOIN orderdetails od
USING (ordernumber)
GROUP BY o.status
HAVING total_revenue > 150000;

