# SOAL 6
-- Tampilkan Jumlah Employees yang terdapat ditiap officecode
SELECT officecode, count(*) jumlah_Employee
FROM employees
GROUP BY officecode;