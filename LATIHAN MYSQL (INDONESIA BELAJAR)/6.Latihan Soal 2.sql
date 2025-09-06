# SOAL 6
-- Tampilkan jumlah employees yang terdapat ditiap country

SELECT o.country, count(*)total_employees
FROM offices o 
INNER JOIN employees e USING (officecode)
GROUP BY o.country;