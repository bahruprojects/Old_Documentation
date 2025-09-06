SHOW databases; -- Menampilkan Database
USE classicmodels; -- Menggunakan classicmodels
SELECT * -- Memilih semua kolom (* = ALL)
FROM employees ; -- Memilih dari employees
DESCRIBE employees; -- Deskripsikan tabel employees
SELECT lastname FROM employees; -- Memilih/menampilkan kolom lastname dari tabel employees

SELECT 
	lastname, 
	firstname, 
    jobtitle 
FROM employees; -- Memilih/menampilkan kolom lastname, firstname, jobtitle dari tabel employees
