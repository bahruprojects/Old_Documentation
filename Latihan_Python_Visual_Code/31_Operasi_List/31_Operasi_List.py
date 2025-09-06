data_angka = [1, 4, 5, 7, 2, 5, 1, 0, 7, 4, 3, 9, 10, 8]

print(f'Data Angka = \n{data_angka}')

# Count Data

jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)

print(f'Jumalh Angka 4 = {jumlah_data_4}')
print(f'Jumalh Angka 3 = {jumlah_data_3}')

# Ambil Posisi Data (Index)

data = ['Alfin', 'Bahru', 'Rahmika', 'Umar']
print(f'Data = {data}')

index_rahmika = data.index('Rahmika')
index_alfin = data.index('Alfin')

print(f'index_rahmika = {index_rahmika}')
print(f'index_alfin = {index_alfin}')

# Mengurutkan List (Sorting)

## Sebelum Sorting 
print(f'Data Angka Sebelum Sort = \n{data_angka}')
## Sesudah Sorting
data_angka.sort()
print(f'Data Angka Sesudah Sort = \n{data_angka}')

## Mengurutkan Data String
print(f'Data  = \n{data}')
data.sort()
print(f'Data Sort = \n{data}')

# Balik Listnya
data_angka.reverse()
data.reverse()
print(f'Data Angka Sesudah Sort Di Reverse = \n{data_angka}')
print(f'Data Sesudah Sort Di Reverse = \n{data}')



