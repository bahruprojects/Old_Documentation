## Global Dan Local Scope
print('\n')
import os
os.system('cls')

nama_global = 'Alfin' # Variabel Global

# Akses Variabel Global Dalam Fungsi
def fungsi():
    print(f'Fungsi Menampilkan {nama_global}')
fungsi()

# Akses Variabel Global Dalam Loop
for i in range(0, 5):
    print(f'Loop {i} - {nama_global}')

# Percabangan
    if True:
        print(f'If Menampilkan Nama Global = {nama_global}')

## Variabel Local Scope

def fungsi2():
    nama_local = 'Alfin' # Variabel Lokal

fungsi2()
# print(nama_local) # Tidak Bisa Dilakukan


## Contoh Penggunaan

## Contoh 1:Penggunaan Akses Variabel
def say_bahru():
    print(f'Hello {nama}')

nama = 'bahru'
say_bahru()

## Contoh 2: Merubah Variabel Global
angka = 0
name = 'Rahmika'

def ubah_angka(nilai_baru, nama_baru):
    global angka  # Fungsi Ini Mendapat Akses Merubah Angka
    global name
    angka = nilai_baru
    name = nama_baru

print(f'Sebelum {angka, name}')
ubah_angka(10, 'Rahmika')
print(f'Sesudah {angka, name}')

## Contoh 3:
angka = 0

for i in range (0, 5):
    angka += i 
    angka_dummy = 0

print(angka)
print(angka_dummy)


if True:
    angka = 10
    angka_dummy = 10

print(angka)
print(angka_dummy)






