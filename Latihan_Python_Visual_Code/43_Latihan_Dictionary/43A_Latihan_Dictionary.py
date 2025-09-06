# Fromkeys

# Template Dict Mahasiswa
import datetime
import os

mahasiswa_template = {
    'nama' : 'nama',
    'nim'  : '000000',
    'sks_lulus' : 0,
    'lahir' : datetime.datetime(1111,1,11)
}

data_mahasiswa = {}
os.system('cls')
print(f'{'SELAMAT DATANG' :^20}')
print(f'{'DATA MAHASISWA' :^20}')
print('-'*20)

mahasiswa = dict.fromkeys(mahasiswa_template.keys())
print(mahasiswa)
mahasiswa['nama'] = input('Nama Mahasiswa : ')
mahasiswa['nim'] = input('NIM Mahasiswa : ')
mahasiswa['sks_lulus'] = int(input('SKS Lulus : '))
TAHUN_LAHIR = int(input('Tahun Lahir (YYYY) : '))
BULAN_LAHIR = int(input('Bulan Lahir (1-12) : '))
Tanggal_LAHIR = int(input('Tanggal Lahir (1-31) : '))
mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR, Tanggal_LAHIR)

print(mahasiswa)















