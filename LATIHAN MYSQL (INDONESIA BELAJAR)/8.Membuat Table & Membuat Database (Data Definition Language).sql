-- Membuat Table & Membuat Database (Data Definition Language)

-- Membuat Database
CREATE DATABASE test_db;

-- Menghapus Database
DROP DATABASE test_db;

# CONTOH PEMBUATAN

-- Membuat Databases Kampus
CREATE DATABASE Kampus;
USE Kampus;

-- Membuat Table
CREATE TABLE Mahasiswa(
	NIM varchar(8) not null,
    Nama varchar(50),
    Alamat varchar(150),
    IPK float,
    primary key(NIM)
);
SHOW tables;
DESCRIBE mahasisiswa;

-- Menghapus Table
DROP TABLE Mahasiswa;

-- Menambahkan Kolom Kota_Kelahiran
ALTER TABLE Mahasiswa ADD Kota_Kelahiran varchar(50);

-- Memodifikasi Kolom Kota_Kelahiran menjadi Kota_Asal
ALTER TABLE Mahasiswa change column Kota_Kelahiran Kota_Asal varchar(60);

-- Menghapus Kolom Alamat Pada Mahasiswa
ALTER TABLE Mahasiswa DROP column Alamat;

-- Mengubah nama 'Table' Mahasiswa menjadi 'Siswa'
ALTER TABLE Mahasiswa RENAME TO Siswa;