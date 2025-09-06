"""ARGS"""
import os
os.system('cls')
print('\n')

def fungsi(nama, tinggi, berat):
    print(f'{nama} Punya Tinggi {tinggi} Dan Berat {berat}')

fungsi('Alfin',170,40)

# Fungsi Diatas Menggunakan List

def fungsi (data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f'{nama} Punya Tinggi {tinggi} Dan Berat {berat}')
fungsi(['Bahru', 190, 100])


# Fungsi Dengan Args

def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f'{nama} Punya Tinggi {tinggi} Dan Berat {berat}')
fungsi('Rahmika', 180, 80)


# Studi Kasus
def tambah(*data):
    # Data Tipenya Adalah Tuple, Dia Bisa Diiterasi
    output = 0
    for angka in data:
        output += angka
    return output

hasil = tambah(1,2,3,4,5,6,7,8,9)
print(f'Hasil = {hasil}')

hasil = tambah(10, 25, 50)
print(f'Hasil = {hasil}')





