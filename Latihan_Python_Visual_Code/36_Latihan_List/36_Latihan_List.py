# PROGRAM LIST BUKU
print('\nPROGRAM LIST BUKU\n')

list_buku = []
while True:

    judul = input('Masukkan Judul Buku\t : ')
    penulis = input('Masukkan Nama Penulis\t : ')


    buku_baru = [judul, penulis]
    list_buku.append(buku_baru)


    print('No.| Judul  | Penulis')

    print('\n\n','='*10,'DATA BUKU','='*10)

    for index, buku in enumerate(list_buku):
        print(f'{index} | {buku[0]} | {buku[1]}')


    print('\n\n','='*20)
    isLanjut  = input('Apakah Dilanjutkan ?(y/n)  ')

    if isLanjut == 'n':
        break

print('PROGRAM SELESAI')




























