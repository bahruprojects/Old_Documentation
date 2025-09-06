# Soal 7
-- Buatkan Query untuk menampilkan country dengan jumlah employees dibawah 8

SELECT o.country, e.officecode, count(e.officecode)
jumlah_employees
FROM offices o INNER JOIN employees e 
USING (officecode)
GROUP BY country
HAVING jumlah_employees < 8;