# SOAL 3

SELECT ordernumber, productcode, quantityOrdered
FROM orderdetails
WHERE quantityOrdered > 40
ORDER BY quantityOrdered