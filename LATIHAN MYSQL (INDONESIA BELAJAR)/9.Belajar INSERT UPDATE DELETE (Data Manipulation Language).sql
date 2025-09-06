-- Belajar INSERT UPDATE DELETE (Data Manipulation Language)

-- Contoh Membuat Database, Namanya "Kuliah"
CREATE DATABASE Kuliah;
SHOW DATABASES;
USE Kuliah;

-- Contoh Membuat Table, Namanya "Mahasiswa"
CREATE TABLE Mahasiswa (
NIM varchar(10) NOT NULL,
Nama varchar(50),
Kota varchar(150),
IPK float,
primary key (NIM));

SHOW Tables;
DESCRIBE Mahasiswa;

-- Menambahkan Data Pada Table
INSERT INTO Mahasiswa
values('111', 'Bejo', 'Bogor', 2.24);

SELECT * FROM Mahasiswa;

-- Menginput Data Baru
INSERT INTO Mahasiswa(NIM, Nama)
Values ('222', 'Tejo');

INSERT INTO Mahasiswa(Nama, IPK, NIM)
Values ('Cecep', 1.58, '333');

INSERT INTO Mahasiswa(NIM, Nama, Kota)
Values('444', 'Wati', 'Semarang'),
('555', 'Ani', 'Surabaya'),
('666', 'Rati', 'Malang');

-- Mengubah Data pada suatu Tabel

UPDATE Mahasiswa
SET Kota='Sidoarjo'
WHERE NIM = '555';

UPDATE Mahasiswa
SET Kota ='Bekasi', IPK = 3.55
WHERE NIM = '222';

-- Menghapus Data Pada Tabel
DELETE FROM Mahasiswa
WHERE NIM = '444';