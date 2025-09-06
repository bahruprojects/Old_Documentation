 # Operasi String Dengan Method

## Merubah Case Dari String

### Merubah Ke Uppercase
print('\n\n')
x = 'Bahru'
print('nama =  ' + x)
x = x.upper()
print('upper = ' + x)

print('\n\n')

### Merubah Ke Lowercase
y = 'Alfin'
print('nama =  ' + y)
y = y.lower()
print('lower = ' + y)

print('\n\n')

## Pengecekan Dengan Is Method
# Contoh Untuk Pengecekan Lower Case
z = 'rahmika'
apakah_lower = z.islower()
print(z + ' is lower = ' + str(apakah_lower))

# Contoh Untuk Pengecekan Upper Case
z = 'rahmika'
apakah_upper = z.isupper()
print(z + ' is upper = ' + str(apakah_upper))

# isalpha() (Untuk Menecek Apakah Semuanya Huruf)
# isalnum() (Untuk Huruf & Angka)
# isdecimal() (Angka Saja)
# isspace() (Spasi, Tab, Newline)
# istitle() (Semua Kata Dimulai Dengan Huruf Besar

title = "I am not okay"

cek_title = title.istitle()
print(title + " is title = " + str(cek_title))


## Ngecek Komponen startswith() endswith()
cek_start = "My Chemical Romance".startswith("My")
print("Start = ", str(cek_start))

cek_end = "My Chemical Romance".endswith("Romance")
print("End = ", str(cek_end))

# Penggabungan Komponen join() split()
list = ["Alfin", "Bahru", "Rahmika"]
gabungan = " , ".join(list)
print(list)
print(gabungan)


gabungan = ' '.join(list)
print(gabungan)

gabungan = 'T'.join(list)
print(gabungan)

gabungan = 'AlfinTBahruTRahmika'
pisah = gabungan.split('T')
print(pisah)

# Alokasi Karakter rjust(), ljust(), center()

right = 'alfin'.rjust(10)
print(right)

left = 'alfin'.ljust(10)
print(left)

middle = 'alfin'.center(50)
print(middle)

middle2 = 'alfin'.center(30, '!')
print(middle2)

# Kebalikannya (pAkaia Strip())
print(middle2)
middle3 = middle2.strip('!')
print(middle3)

print('\n\n')












































