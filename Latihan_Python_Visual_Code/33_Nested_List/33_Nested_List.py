#  NESTED LIST / LIST BERSARANG

data_0 = [1, 2]
data_1 = [3, 4]

data_list_biasa = [1, 2, 3, 4]

print(f'List Biasa = {data_list_biasa }')

list_2D = [data_0, data_1, 6, 7]

print(f'List 2D= {list_2D}')

# Contoh Penggunaan

peserta_0 = ['Ucup', 25, 'Laki-Laki']
peserta_1 = ['Otong', 10, 'Laki-Laki']
peserta_2 = ['Dedeh', 50, 'Wanita']

list_peserta = [peserta_0, peserta_1, peserta_2]

print(f'list_peserta = {list_peserta}')

for peserta in list_peserta:
    print(f'nama\t: {peserta[0]}')
    print(f'umur\t: {peserta[1]}')
    print(f'gender\t: {peserta[2]}\n')



# Dengan Referance 
    
list_copy = list_peserta.copy();
print(f'peserta = {list_copy}')

peserta_0[0] = 'Michael'
print(f'peserta = {list_copy}')
print(f'peserta = {list_peserta}')














