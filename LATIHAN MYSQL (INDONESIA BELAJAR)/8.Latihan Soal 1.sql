# SOAL 8

-- Membuat Table Barang. KOLOM Kode Barang & Nama Barang Dengan tipe data Varchar
CREATE DATABASE TOKO;
USE TOKO;

CREATE TABLE Barang(
	Kode_Barang varchar(10),
    Nama_Barang varchar(50),
    Primary key (Kode_Barang)
);
SHOW TABLES;
DESCRIBE Barang;