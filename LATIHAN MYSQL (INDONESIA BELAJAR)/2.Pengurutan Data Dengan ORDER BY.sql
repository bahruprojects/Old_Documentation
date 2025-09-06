SHOW databases;
USE classicmodels;
SHOW tables;
DESCRIBE employees;
SELECT * FROM employees;

SELECT * 
FROM employees
ORDER BY lastname; -- Mengurutkan data berdasarkan ''lastname'' secara alfabetik (secara ascending)

SELECT * 
FROM employees
ORDER BY lastname DESC; -- Mengurutkan data berdasarkan ''lastname'' secara alfabetik (secara descending)

SELECT * 
FROM employees
ORDER BY lastname, firstname; -- Mengurutkan data berdasarkan ''lastname'' secara alfabetik (secara ascending) terlebih dahulu, lalu diurutkan ke firstname

SELECT * 
FROM employees
ORDER BY lastname, firstname DESC; -- Mengurutkan data berdasarkan ''lastname'' secara alfabetik (secara ascending) terlebih dahulu, lalu diurutkan ke firstname secara descending

SELECT lastname, firstname, jobtitle
FROM employees
ORDER BY lastname;

DESCRIBE orderdetails;

SELECT ordernumber, quantityOrdered * priceEach
FROM orderdetails;

SELECT ordernumber, quantityOrdered * priceEach
FROM orderdetails
ORDER BY quantityOrdered * priceEach;

SELECT ordernumber, quantityOrdered * priceEach
FROM orderdetails
ORDER BY quantityOrdered * priceEach DESC;

SELECT ordernumber, (quantityOrdered * priceEach) AS subtotal
FROM orderdetails
ORDER BY subtotal * priceEach DESC;