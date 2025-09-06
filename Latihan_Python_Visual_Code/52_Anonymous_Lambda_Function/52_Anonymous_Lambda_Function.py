"""LAMBDA FUNCTION"""
import os
os.system('cls')
print('\n')

def fungsi_kuadrat(angka):
    return angka**2
print(f'Hasil Fungsi Kuadrat = {fungsi_kuadrat(3)}')

# Kita Coba Pakai Lambda
# Output = Lambda Argument: Expression

kuadrat = lambda angka:angka**2
print(f'Hasil Lambda Kuadrat = {kuadrat(5)}')

# Dua Input
pangkat = lambda num,pow : num**pow
print(f'Hasil Lambda Pangkat = {pangkat(4,2)}')

# Kegunaan
# Sorting Untuk List
data_list = ['Alfin', 'Bahru', "Rahmika"]
data_list.sort()
print(f'Sorted List = {data_list}')

# Sorting Dia Pakai Panjang
def panjang_nama(nama):
    return len(nama)

data_list.sort(key = panjang_nama)
print(f'Sorted List By Panjang {data_list}')

# Sort Pakai Lambda
data_list= ['Alfin', 'Bahru', 'Rahmika']
data_list.sort(key = lambda nama:len(nama))
print(f'Sorted List By Lambda = {data_list}')

# Sort Pakai Filter
data_angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
def kurang_dari_lima(angka):
    return angka <5

data_angka_baru = list(filter(kurang_dari_lima, data_angka))
data_angka_baru = list(filter(lambda x:x<5, data_angka))
print(data_angka_baru)

# Kasus Genap
data_genap = list(filter(lambda x:(x%2==0), data_angka))
print(data_genap)

# Kasus Ganjil
data_ganjil = list(filter(lambda x:(x%2!=0), data_angka))
print(data_ganjil)

# Kelipatan 3
data_3 = list(filter(lambda x:(x%3==0), data_angka))
print(data_3)

# Anonymous Function
# Currying <- Haskell Curry

def pangkat(angka, n):
    hasil = angka**n
    return hasil
data_hasil = pangkat(5,2)
print(f'Fungsi Biasa = {data_hasil}')


# Dengan Currying Menjadi
def pangkat(n):
    return lambda angka:angka**n
pangkat2 = pangkat(2)
print(f'Pangkat 2 = {pangkat2(5)}')

pangkat3 = pangkat(3)
print(f'Pangkat 3 = {pangkat3(4)}')

print(f'Pangkat Bebas = {pangkat(4)(5)}')
