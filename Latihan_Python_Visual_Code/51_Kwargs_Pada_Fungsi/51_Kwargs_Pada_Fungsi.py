# Kwargs
import os
os.system('cls')
print('\n')

def fungsi(nama, tinggi, berat):
    """Fungsi Biasa"""
    print(f'{nama} Punya Tinggi {tinggi} Dan Berat {berat}')
fungsi('Alfin', 185, 80)


def fungsi(**kwargs):
    """Fungsi Biasa"""
    nama = kwargs['nama']
    tinggi = kwargs['tinggi']
    berat = kwargs['berat']
    print(f'{nama} Punya Tinggi {tinggi} Dan Berat {berat}')
fungsi(nama = 'Bahru', tinggi = 200, berat = 90)


# Studi Kasus

def math(*args, **kwargs):
    output = 0
    if kwargs['option'] == 'tambah':
        for angka in args :
            output += angka

    elif kwargs['option'] == 'kali':
        output = 1
        for angka in args :
            output *= angka
    else:
        print('Tidak Ada Operasi')

    return output

hasil = math(1, 2, 3, 4, 5, 6, option='tambah')
print(f'Hasil Jumlah {hasil}')

hasil = math(1, 2, 3, 4, 5, 6, option='kali')
print(f'Hasil Kali {hasil}')


















