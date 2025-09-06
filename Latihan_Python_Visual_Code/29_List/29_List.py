# LIST

# Kumpulan Data Numbers
data_angka = [1, 5, 2, 3]
print(data_angka)


# Kumpulan Data String
data_string = ['Alfin', 'Bahru', 'Rahmika']
print(data_string)

# Kumpulan Data Boolean
data_boolean = [True, False, True, True]
print(data_boolean)

# Kumpulan Campuran
data_campuran = [1, 'tes tes tes', 2, 'Alfinn', 'Bahru', True, 'Rahmika', False]
print(data_campuran)

# Cara Alternatif Membuat List 
data_range = range(0, 10, 2) # Range (Start, Stop, Steps)
print(data_range)
data_list = list(data_range)
print(data_list)

# Membuat List Dengan For Loop, List Comprehension
list_pake_for = [i for i in range (0,10)]
print(list_pake_for)

list_pake_for = [i**2  for i in range (0,10)] # Buat Kuadrat Dari List
print(list_pake_for)

# Membuat List Pake For Pake If
lis_pake_for_if = [i for i in range(0,10) if i !=5]
print(lis_pake_for_if )

lis_pake_for_if = [i for i in range(0,10) if i%2 == 0] # List Genap
print(lis_pake_for_if)

lis_pake_for_if = [i for i in range(0,10) if i%2 != 0] # List Ganjil
print(lis_pake_for_if)

lis_pake_for_if = [i**2 for i in range(0,10) if i%2 != 0] # List Ganjil Kuadrat
print(lis_pake_for_if)







