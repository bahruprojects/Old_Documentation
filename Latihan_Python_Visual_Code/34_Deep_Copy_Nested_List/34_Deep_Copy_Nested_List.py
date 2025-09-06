data_0 = [1, 2]
data_1 = [3, 4]

data_2D = [data_0, data_1]
data_2D_copy = data_2D.copy()

# Memunculkan Nested List (List Bersarang)
print(f'data = {data_2D}')
print(f'data Copy = {data_2D_copy}')

# Mengambil Data Dalam List Bersarang

data = data_2D[1][0]
print(f'data = {data}') # Akan Muncul '3'
print(f'data = {data}')

# Address Semuanya
print(f'Address asli = {hex(id(data_2D))}')
print(f'Address copy = {hex(id(data_2D_copy))}')


print('Address Dari Member Ke-1')
print(f'Address asli = {hex(id(data_2D[0]))}')
print(f'Address copy = {hex(id(data_2D_copy[0]))}')

# Data Copy dan Original, Address-nya beda tapi address member sama

# MENGGUNAKAN DEEP COPY
from copy import deepcopy

data_2D = [data_0, data_1, 10]
data_2D_deepcopy = deepcopy(data_2D)

# Address Semuanya

print(f'Address asli = {hex(id(data_2D))}')
print(f'Address deepcopy = {hex(id(data_2D_deepcopy))}')

print('Address Dari Member Ke-1')

print(f'Address asli = {hex(id(data_2D[0]))}')
print(f'Address deepcopy = {hex(id(data_2D_deepcopy[0]))}')



