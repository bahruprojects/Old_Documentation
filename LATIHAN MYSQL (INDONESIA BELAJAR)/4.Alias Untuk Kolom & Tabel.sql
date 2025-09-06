-- Alias Untuk Kolom & Tabel

SHOW databases;
USE classicmodels;
SHOW tables;


SELECT firstname, lastname
FROM employees;

SELECT CONCAT (firstname,' ',lastname)
FROM employees; -- Menggabungkan firstname dan lastname

SELECT CONCAT (firstname,'-',lastname, '-', email)
FROM employees; 

SELECT CONCAT_WS ('-', firstname, lastname, email)
FROM employees; 

SELECT firstname, lastname,
		CONCAT_WS (' ',firstname, lastname)
FROM employees; 

SELECT firstname, lastname,
		CONCAT (firstname, ' ', lastname) AS FullName
FROM employees; -- Alias pada kolom

SELECT firstname, lastname,
		CONCAT_WS (' ',firstname,lastname) AS FullName
FROM employees; 

SELECT firstname, lastname,
		CONCAT_WS (' ',firstname,lastname) FullName
FROM employees; 

SELECT firstname, lastname,
		CONCAT_WS (' ',firstname,lastname) FullName
FROM employees
ORDER BY fullname;

SELECT e.firstname, e.lastname
FROM employees e; -- Pemberian Alias pada Tabel


SELECT e.firstname, e.lastname
FROM employees e
ORDER BY e.lastname;