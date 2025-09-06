# Width Dan Multiline 
print('\n')

data_nama = 'Alfin Bahru'
data_umur = 20
data_tinggi = 170.02
data_nomor_setapu = 45

# String Standard
data_string = f"nama {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_nomor_setapu}"

print(5*'='+"Data String" + 5*'=')
print(data_string)



# String Multiline
data_string = f"nama {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nsepatu = {data_nomor_setapu}"

print('\n'+5*'='+"Data String" + 5*'=')
print(data_string)


# String Multiline Dengan Kutip Triplets (""")
data_nama = 'Alfin'

data_string = f"""
nama    = {data_nama}
umur    = {data_umur}
tinggi  = {data_tinggi}
sepatu  = {data_nomor_setapu}
"""

print('\n'+5*'='+"Data String" + 5*'=')
print(data_string)

# Mengatur Lebar

data_string = f"""
nama    = {data_nama}
nama    = {data_nama:>6}
nama    = {data_nama:>10}
umur    = {data_umur}
umur    = {data_umur:>5}
tinggi  = {data_tinggi}
sepatu  = {data_nomor_setapu}
"""

print('\n'+5*'='+"Data String" + 5*'=')
print(data_string)




























































