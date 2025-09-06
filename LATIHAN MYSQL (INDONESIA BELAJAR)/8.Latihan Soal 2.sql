# SOAL 8

-- Tambahkan Kolom baru pada tabel barang, dengan nama kolom 'harga' tipe datanya integer
USE TOKO;
SHOW TABLES;
DESCRIBE Barang;

ALTER TABLE Barang 
ADD Harga int(100);

DESCRIBE Barang;