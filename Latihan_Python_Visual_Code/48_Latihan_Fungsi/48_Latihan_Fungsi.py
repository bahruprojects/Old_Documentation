# # Latihan Fungsi

# # Membuat Program Untuk Menghitung Luas Dan Keliling Persegi Panjang

# import os

# # Membuat Header Program

# os.system('cls')
# print('\n')
# print(f'{"PROGRAM MENGHITUNG LUAS" :^40}')
# print(f'{"DAN KELILING PERSEGI PANJANG" :^40}')
# print(f'{'-'*40:^40}')


# # Mengambil Input User
# LEBAR = int(input('Masukkan Nilai Lebar : '))
# PANJANG = int(input('Masukkan Nilai Panjang : '))

# # Program Menghitung Luas
# LUAS = PANJANG*LEBAR
# KELILING  = 2 *(PANJANG+LEBAR)

# # Tampilkan Hasilnya
# print(f'Hasil Perhitungan Luas = {LUAS}')
# print(f'Hasil Perhitungan Keiling = {KELILING}')



import os
def header():
    """Fungsi Header"""
    os.system('cls')
    print('\n')
    print(f'{"PROGRAM MENGHITUNG LUAS" :^40}')
    print(f'{"DAN KELILING PERSEGI PANJANG" :^40}')
    print(f'{'-'*40:^40}')

def input_user():
    """FUNGSI INPUT USER"""
    LEBAR = int(input('Masukkan Nilai Lebar : '))
    PANJANG = int(input('Masukkan Nilai Panjang : '))
    return LEBAR, PANJANG

def hitung_luas(LEBAR, PANJANG):
    """FUNGSI LUAS"""
    return LEBAR*PANJANG

def hitung_keliling(LEBAR, PANJANG):
    """FUNGSI KELILING"""
    return 2*(PANJANG + LEBAR)

def display(message, value):
    print(f'{message} = {value}')

# Program Utamanya
while True :
    header()
    LEBAR, PANJANG = input_user()
    LUAS = hitung_luas(LEBAR,PANJANG)
    KELILING = hitung_keliling(LEBAR,PANJANG)

    display('LUAS', LUAS)
    display('KELILING', KELILING)

    isContinue = input('Apakah Lanjut (y/n) ?')
    if isContinue == 'n':
        break

print('Program Selesai, Terima Kasih')








































































