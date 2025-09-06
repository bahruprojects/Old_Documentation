# MEMBUAT KALKULATOR SERDEHANA
print('\n')

print(10*'=')
print('KALKULATOR SEDERHANA')
print(10*'=' + '\n')

angka_1 = float(input('Masukkan angka 1 =     '))
operator = input('Operator (+,-,x,/) :     ')
angka_2 = float(input('Masukkan angka 2 =     '))


# Percabangannya

if operator =="+":
    hasil = angka_1 + angka_2
    print(f'Hasilnya adalah {hasil}')
elif operator =="-":
    hasil = angka_1 -  angka_2
    print(f'Hasilnya adalah {hasil}')
elif operator =="x" or operator =="*"  :
    hasil = angka_1 *  angka_2
    print(f'Hasilnya adalah {hasil}')
elif operator =="/" or operator ==":":
    hasil = angka_1 / angka_2
    print(f'Hasilnya adalah {hasil}')

print('Programm Selesai')















