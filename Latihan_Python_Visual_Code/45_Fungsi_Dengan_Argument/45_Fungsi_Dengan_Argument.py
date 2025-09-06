# Fungsi Dengan Argumenn

# def nama_fungsi(argument): 
      #Badan Fungsi
print('\n')

def hello_world(nama):
    print(f'Selamat Datang Dunia Wahai {nama}')

hello_world('Alfin')

# Program Tambah
def tambah(angka_1, angka_2):
    hasil = angka_1 + angka_2
    print(f'{angka_1} + {angka_2} = {hasil}')

tambah(1,5) # Hasilnya 6


# Program Coba-Coba
def say_hi(peserta):
    data_peserta = peserta.copy()
    for peserta in data_peserta:
        print(f'Yang Terhormat {peserta}')

anggota = ['Alfin', 'Rena', 'Baron']

say_hi(anggota) # 'anggota' berubah menjadi 'peserta'



































