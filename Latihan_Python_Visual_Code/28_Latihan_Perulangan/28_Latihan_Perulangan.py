#                                       Latihan Perulangan 

banyak = 10
# 1. Menggunakan 'For
print('\n')
print('AWAL DARI FOR')

# dummy variable
x = 1
for i in range(banyak):
    print('*' * x)
    x = x + 1

print('AKHIR DARI FOR')
print('\n')

# 2. Menggunakan 'While'
print('AWAL DARI WHILE')

x = 1
while True:
    print('*' * x)
    x = x + 1

    if x > banyak:
        break
print('AKHIR DARI WHILE')
print('\n')

# 3. Hanya Ganjil Saja
print('AWAL DARI FOR')

x = 1
while True:
    if (x%2):
        # Print Jika Ganjil
        print('*' * x)
        x +=1
    else:
        # Akan Kembabli Ke Atas Jika Ganjil
        x +=1
        continue
        #Akan Break Jika Melebihi Banyak
    if x > banyak:
        break

print('AKHIR DARI WHILE')
print('\n')


# 4. Segitiga Sama Kaki
print('AWAL DARI FOR')

x = 1
spasi = int(banyak/2)
while True:
    if (x%2):
        # Print Jika Ganjil
        print(" " * spasi , '+' * x)
        spasi = spasi - 1 
        x +=1
    else:
        # Akan Kembabli Ke Atas Jika Ganjil
        x +=1
        continue
        #Akan Break Jika Melebihi Banyak
    if x > banyak:
        break

print('AKHIR DARI WHILE')
print('\n')
































































