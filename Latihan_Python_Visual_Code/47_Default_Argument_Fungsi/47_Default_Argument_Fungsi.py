import os
os.system('cls')
# def fungsi (argument):
# def fungsi(argument = nilai defaultnya):
print('\n')

# Contoh 1
def say_hello(nama = 'Ganteng'):
    '''Fungsi Dengan Default Argument'''
    print(f'Hallo {nama}')
say_hello('Alfin')
say_hello()
print('\n')

# Contoh 2
def sapa_dia(nama, pesan = 'Apa Kabar ?'):
     '''Fungsi Dengan Satu Input Biasa, Dan Satu Default Argument'''
     print(f'hai {nama}, {pesan}')
    
sapa_dia('Dudung', 'Hai Ganteng')
sapa_dia('Otong')
print('\n')

# Contoh 3
def hitung_pangkat(angka, pangkat):
     hasil = angka**pangkat
     return hasil
print(hitung_pangkat(2,4))

hasil = hitung_pangkat(pangkat=3, angka=5)
print(hasil)
print('\n')

# Contoh 4
def fungsi(input1 = 1, input2 = 2, input3 = 3, input4 = 4):
     hasil = input1 + input2 + input3 + input4
     return hasil

print(fungsi())
print(fungsi(input3 = 10))












