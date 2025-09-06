# Operator dictionary
print('\n')

data_dict = {
    "cup" : 'Ucup Surucup',
    'tong' : 'Otong Sirotong',
    'dung' : 'Dudung Surudung'
}

# Panjag Dictionary
lendict = len(data_dict)
print(f'Panjang Dictionary : {lendict}')

# Mengecek Key Exist Atau Tidak
Key = 'cup'
CHECKKEY = Key in data_dict
print(f'Apakah {Key} ada di data_dict : {CHECKKEY}')

# Mengakses Value Dengan Fungsi 'Get'
print(data_dict['cup'])
print(data_dict.get('cup'))
print(data_dict.get('kis', 'Key Tidak Ditemukan')) # Cek Key Dengan Message Tidak Ditemukan

# Mengupdate Data
data_dict['cup'] = 'ucup si ganteng'
print(data_dict)

# Menambah Data
data_dict['sep'] = 'asep si kasep'
print(data_dict)

data_dict.update({'cup' : 'Ucup Surucup'})
print(data_dict)

data_dict.update({'faqih' : 'Faqihzaaah'})
print(data_dict)

# Mendelete Data Pada Dictionary
del data_dict['faqih']
print(data_dict)





















