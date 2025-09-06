-- Belajar Subquery (Nested Query)

SHOW DATABASES;
USE classicmodels;
SHOW TABLES;

SELECT * FROM payments
ORDER BY amount DESC;

SELECT max(amount)
FROM payments;

SELECT * FROM payments
WHERE amount = 120166.58;

-- Menggunakan Subquery

SELECT * FROM payments
WHERE amount = (
				SELECT max(amount)
				FROM payments
);

-- 

SELECT e.firstname, e.lastname
FROM employees e INNER JOIN offices o
USING (officecode)
WHERE o.country ='USA';

-- Menggunakan Subquery

SELECT firstname, lastname
FROM employees
WHERE officecode IN (
					SELECT officecode
					FROM offices 
					WHERE country = 'USA'
);

--
SELECT ordernumber, count(*) 'items'
FROM orderdetails 
GROUP BY ordernumber;

SELECT AVG(t1.items), MAX(t1.items), MIN(t1.items)
FROM (
		SELECT ordernumber, count(*) 'items'
		FROM orderdetails 
		GROUP BY ordernumber
) t1;

