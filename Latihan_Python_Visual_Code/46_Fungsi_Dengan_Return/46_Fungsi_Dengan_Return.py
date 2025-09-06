# Fungsi Dengan Kembalian (Return Value)
# Template Fungsi Kembalian
# def nama_fungsi(argument):
        # badan fungsi
        # return output

print('\n')

# Membuat Fungsi Kuadrat

def kuadrat(input):
    output = input**2
    return output

y = kuadrat(3)
print(y)

print(kuadrat(6))

z = 10 + kuadrat (7)
print(z)

# Fungsi Tambah

def tambah(angka_1, angka_2):
    return angka_1 + angka_2
a = tambah(3,8)
print(a)

# Fungsi Dengan Return Banyak
def operasi_matematika(angka_1, angka_2):
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2

    return tambah, kurang, kali, bagi

k, l, m, n = operasi_matematika(9,5)

print(f'Hasil Tambah = {k}')
print(f'Hasil Kurang = {l}')
print(f'Hasil Kali = {m}')
print(f'Hasil Bagi = {n}')























