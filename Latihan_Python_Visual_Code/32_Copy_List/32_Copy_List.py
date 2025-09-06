# Teknik Menduplikat List

a = ['Ucup', 'Otong', 'Dudung']
print(f'a = {a}')

b = a # Pass By Refrence
print(f'b = {b}')

# Kita Akana Merubah Member Dari a
a[1] = 'Michael'
b.sort()
print(f'a = {a}')
print(f'b = {b}')

# Address Dari Kedua List a dan b
print(f'Address a = {hex(id(a))}')
print(f'Address b = {hex(id(b))}')


# Menduplikat List Dengan Copy
print('Membuat list c dengan a.copy()')

c = a.copy() # Full Duplikat / Data Baru
print(f'c = {c}')
print(f'Address a = {hex(id(a))}')
print(f'Address b = {hex(id(b))}')
print(f'Address c = {hex(id(c))}') # NIlai c sama dengan a tapi Address beda

print('Kita Ubah Data 0')
c[0] = 'Dadang'
print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')













