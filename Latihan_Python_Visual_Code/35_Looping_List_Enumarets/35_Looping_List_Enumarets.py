# LOOPING DARI LIST

# Pakai For Loop
print('\nFor Loop\n')
kumpulan_angka = [4, 3, 2, 5, 6, 1]

for angka in kumpulan_angka:
    print(f'Angka = {angka}')

peserta = ['ucup', 'otong', 'dadang', 'diding', 'dudung']

for nama in peserta:
    print(f'Nama = {nama}')

# Pakai For Loop Dan Range
print('\nFor Loop & Range \n')
kumpulan_angka = [10, 5, 4, 2, 6, 5]

panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f'Angka = {kumpulan_angka[i]}')

# Pakai While Loop
print('\nWhile Loop\n')


kumpulan_angka = [10, 5, 4, 2, 6, 5]

panjang = len(kumpulan_angka)

i = 0
while i<panjang :
    print(f'Angka = {kumpulan_angka[i]}')
    i += 1


angka = [10, 5, 4, 2, 6, 5]
angka_kuadrat = [i**2 for i in angka]
print(f'Angka Kuadrat = {angka_kuadrat}')

# Pakai List Comprehension
print('\nList Comprehension\n')

data = ['ucup', 1, 2, 3, 'otong']

[print(f'Data = {i}') for i in data]



# Pakai Enumarets
print('\nEnumarets\n')

data_list = ['ucup', 1, 2, 3, 'otong']

for index,data in enumerate(data_list):
    print(f'Index = {index}, data = {data}')










