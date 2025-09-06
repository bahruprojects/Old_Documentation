# Soal 7
-- Buatkan Query dengan officecode diatas 3

SELECT officecode, count(officecode) total_employees
FROM employees
GROUP BY officecode
HAVING total_employees > 3;