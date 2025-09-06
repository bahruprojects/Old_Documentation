
# Operasi Dan Manipulasi String

# 1. Menyambung STring (Concatenate)
print('\n\n')

nama_pertama ='Alfin'
nama_tengah = 'Bahru'
nama_akhir ='Rahmika'

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap)


# 2. Menghitung Panjang Dari String (Operator Len)
panjang = len(nama_lengkap)

print("Panjang Dari" + nama_lengkap + "=" + str(panjang))

#3. Operator Dari String
# Mengecek Adanya Komponen Char di String
a = 'a'
A = 'A'

status = a in nama_lengkap
print("String" + " a " + "ada di " + nama_lengkap + "=" + str(status))


status = A not in nama_lengkap
print("String" + " a "  + "ada di " + nama_lengkap + "=" + str(status))

#4. Mengulang String
print(' Alfin'*5)
print('#' * 20)

#5. Indexing
# mengetahui index
print(nama_lengkap)
print('Index ke-0 : ' + nama_lengkap[0])
print('Index ke-1 : ' + nama_lengkap[1])
print('Index ke-2 : ' + nama_lengkap[2])
print('Index ke-3 : ' + nama_lengkap[3])
print('Index ke (-1) : ' + nama_lengkap[-1])
print('Index ke (-2) : ' + nama_lengkap[-2])
print('Index ke (-3) : ' + nama_lengkap[-3])

# Rentang
print('Index ke (0,3) : ' + nama_lengkap[0:4])
print('Index ke (3,7) : ' + nama_lengkap[3:8])

# Jeda
print('Index ke (0,2,4,6,8) : ' + nama_lengkap[0:10:2])

# Item Paling Kecil
print('Paling Kecil :  ' + min(nama_lengkap))
# Item Paling Besar
print('Paling Besar:  ' + max(nama_lengkap))

ascii_code = ord(' ')


#4. Operator Dalam Bentuk Method

data = "Pergi ke Universitas Diponegoro"
jumlah = data.count("i")
print("Jumlah i pada " + data + " = " + str(jumlah))































print('\n\n')

























































