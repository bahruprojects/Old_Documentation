# Membuat Gabungan Area Rentang Dari Angka

inputUser = float(input('Masukkan Angka Yang Bernilai\nKurang Dari 3\nAtau \nLebih Besar Dari 10\n:  '))

# Memeriksa Angka Kurang Dari 3
isKurangDari = (inputUser  < 3)
print("Kurang Dari 3 = ", isKurangDari)

# Memeriksa Angka Lebih Dari 10
isLebihDari = (inputUser > 10)
print("Lebih Dari 10 = ", isLebihDari)


# Membuat Gabungan
isCorrect = isKurangDari or isLebihDari
print("Angka Yang Anda Masukkan : ", isCorrect)

# Membuat Irisan

print('\n', 10 * "=" ,"\n" )

inputUser = float(input('Masukkan Angka Yang Bernilai\nLebih Dari 3\nDan \nKurang Dari 10\n:  '))

#Lebih dari 3
isLebihDari = inputUser > 3
print("Lebih Dari 3 = ", isLebihDari)

#Kurang dari 10
isKurangDari = inputUser < 10
print("Kurang Dari 10 = ", isKurangDari)


isCorrect = isKurangDari and isLebihDari
print("Angka Yang Anda Masukkan : ", isCorrect)





















