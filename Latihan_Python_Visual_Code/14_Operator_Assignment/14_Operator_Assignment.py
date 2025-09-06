# Operasi Yang Dapat Dilakukan Dengan Penyingkatan
# Operasi Ditambah Assignment

a = 5 # Adalah Assignment
print('nilai a =', a)

# a = a + 1
# print('nilai a =', a)         # Hasil Menjadi 6


a += 1      # (a = a + 1) bisa ditulis sebagai (a += 1)
print('nilai a+=1, Nilai a  menjadi', a)

a -= 2 # Artinya Adalah a = a - 2
print('Nilai a -=2, Nilai a Menjadi ', a) # Hasilnya Menjadi 4, Karena nilai a = a + 1 = 6, lalu dikurang 2

a *= 5 # Artinya Adalah a = a * 5
print('Nilai a *=5, Nilai a Menjadi ', a) # Hasilnya Menjadi 20, Karena nilai a = a * 5 = 4 * 5

a /= 2 # Artinya Adalah a = a / 2
print('Nilai a /=2, Nilai a Menjadi ', a) # Hasilnya Menjadi 10, Karena nilai a = a / 2 = 20 * 2

b = 10
print('\nnilai B = ', b)

# Modulus Dan Floor Division

# b %= 3
# print('nilai b %= 3, nilai b menjadi ', b)

b //= 2
print('nilai b //= 3, nilai b menjadi ', b)

# Pangkat
a = 5
print('nilai a ', a)
a**= 3
print('nilai a **= 3, nilai a menjadi ', a)

# Operasi Bitwise

# OR (|)
c = True
print('\nnilai C =', c)
c |= False 
print('nilai c |= False, nilai c menjadi ', c)

c = False
print('\nnilai C =', c)
c |= False 
print('nilai c |= False, nilai c menjadi ', c)

# AND (&)
c = True
print('\nnilai C =', c)
c &= False 
print('nilai c &= False, nilai c menjadi ', c)

c = True
print('\nnilai C =', c)
c &= False 
print('nilai c &= False, nilai c menjadi ', c)

c = True
print('\nnilai C =', c)
c &= True
print('nilai c &= True, nilai c menjadi ', c)

# XOR (^)
c = True
print('\nnilai C =', c)
c ^= False 
print('nilai c ^= False, nilai c menjadi ', c)

c = True
print('\nnilai C =', c)
c ^= True
print('nilai c ^= False, nilai c menjadi ', c)

# Geser Geser
d = 0b0100
print('\nnilai d = ', format(d, '04b'))
d >>= 2
print('nilai d >>=2, nilai d menjadi ',format(d, '04b'))
d <<= 1
print('nilai d <<=1, nilai d menjadi ',format(d, '04b'))


























