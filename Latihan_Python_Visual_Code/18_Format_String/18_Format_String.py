# Format String

# Contoh Generic
# String
print('\n')
nama = "Alfin"

format_str = f"hello {nama} "

print(format_str)

print('\n')

# Angka
angka = 2000.5
format_string = "angka =  " + str(angka)
print(format_string)
print('\n')

# Bilangan Angka
angka = 15
format_str = f'bilangan bulat = {angka:d}'
print(format_str)
print('\n')

#Bilangan Ordo Ribuan
angka = 2000
format_str = f'bilangan ribuan = {angka:,}'
print(format_str)
print('\n')

#Bilangan Ordo Jutaan
angka = 2000000
format_str = f'Jutaan= {angka:,}'
print(format_str)
print('\n')

#Bilangan Desimal
angka = 1050.5545
format_str = f'desimal = {angka:.2f}' # 2 Angka Di Belakang Koma, Float
print(format_str)
print('\n')

#Menampilkan Leading Zero
angka = 1050.5545
format_str = f'desimal = {angka:08.2f}' # menambahkan 0 di Depan Bilangan
print(format_str)
print('\n')

# Menampilkan Tanda "+" Atau "-"

angka_minus = -10
angka_plus = 10
format_minus = f'minus = {angka_minus:+d}'
format_plus = f'plus = {angka_plus:+d}'
print(format_minus)
print(format_plus)
print('\n')

#Memformat Persen

Persentase = 0.045
format_persen = f'persen ={Persentase:.2%}'

print(format_persen)
print('\n')

# Boolean
boolean = True
format_str = f'boolean = {boolean}'
print(format_str)

print('\n')

# Operasi Matematika di Dalam Placeholder
harga = 10000
jumlah = 5

format_string = f'harga total = Rp. {harga*jumlah:,}'
print(format_string)
print('\n')

# Format Angka Lain (Binary, Octal, Hexadecimal)
angka = 255
format_binary = f'binary = {bin(angka)}' 
format_octal = f'octal = {oct(angka)}'
format_hex = f'hex = {hex(angka)}'

print(format_binary)
print(format_octal)
print(format_hex)






























































