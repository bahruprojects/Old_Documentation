-- Seleksi Baris Dengan WHERE

SHOW databases;
USE classicmodels;
SHOW tables;
DESCRIBE employees;

SELECT lastname, firstname, jobtitle, officecode
FROM employees
WHERE jobtitle = 'Sales Rep';

SELECT lastname, firstname, jobtitle, officecode
FROM employees
WHERE jobtitle = 'Sales Rep' AND officecode = 1;


SELECT lastname, firstname, jobtitle, officecode
FROM employees
WHERE jobtitle = 'Sales Rep' OR officecode = 1;

SELECT lastname, firstname, jobtitle, officecode
FROM employees
WHERE jobtitle = 'Sales Rep' OR officecode = 1
ORDER BY officecode, jobtitle;

SELECT lastname, firstname, jobtitle, officecode
FROM employees
WHERE officecode BETWEEN 1 AND 3
ORDER BY officecode, jobtitle;

SELECT lastname, firstname, jobtitle, officecode
FROM employees
WHERE lastname LIKE '%son'
ORDER BY officecode, jobtitle; -- Menampilkan employee dimana Lastname yang diakhiri dengan 'son'

SELECT lastname, firstname, jobtitle, officecode
FROM employees
WHERE firstname LIKE '_a%'
ORDER BY officecode, jobtitle; -- Menampilkan employee dimana firstname dengan huruf keduanya 'a'

SELECT lastname, firstname, jobtitle, officecode
FROM employees
WHERE officecode IN (1, 3, 7)
ORDER BY officecode, jobtitle; -- Menampilkan employee dimana officecode dengan nilai 1, 3 dan 7

SELECT lastname, firstname, jobtitle, officecode
FROM employees
WHERE officecode > 5
ORDER BY officecode, jobtitle; -- Menampilkan employee dimana officecode lebih besar dari 5

SELECT lastname, firstname, reportsTo
FROM employees
WHERE reportsTo IS NULL; -- Menampilkan employees yang reportsto kosong
