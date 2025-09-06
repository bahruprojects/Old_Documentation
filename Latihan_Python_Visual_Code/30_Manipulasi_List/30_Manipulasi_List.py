#      OPERASI
# Index
data = ['Alfin', 'Bahru', 'Rahmika']

# Mengambil Data Dari List
data_0 = data[0]
print(f'data pertama (index 0) = {data_0}')

data_terakhir = data[-1]
print(f'data terakhir = {data_terakhir}')

data_1 = data[1]
data_2 = data[2]
data_min1 = data[-1]
data_min2 = data[-2]
data_min3 = data[-3]
print("data_1",'=', data_1)
print("data_2" ,'=', data_2)
print("data_min1" ,'=', data_min1)
print("data_min2" ,'=', data_min3)
print("data_min1" ,'=', data_min3)

# Mengetahui Panjang Data
panjang_data = len(data)
print(f'Panjang Data = {panjang_data}')

# Memanipulasi List

## Menambahkan item pada list sesuai posisi

print(f'Data Sebelum Ditambah = \n{data}')
# data.insert(posisi, item)
data.insert(1, "tes")
print(f'Data Sesudah Ditambah = \n{data}')


## Menambahkan Di Akhir List

data.append('Eksperimen')
print(f'Data Ditambah Lagi= \n{data}')

## Menambahkan List Dengan List
data_baru = ['Shunya', 'Yeshi', 'Veicinlun']
data.extend(data_baru)
print(f'Data Gabungan = \n{data}')


# Merubah Data
# Kita Ubah Data 2 Menjadi Michael
data[2]='Michael'
print(f'Data Rubah = \n{data}')


# Menghapus Data
data.remove('Shunya')
print(f'Data Remove = \n{data}')

# Meremove Data Paling Belakang
data.pop()
print(f'Data Akhir =\n{data}')











