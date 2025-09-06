# Operasi Komparasi
# Setiap Hasil Adalah Boolean
# >,<,>=,<=,==,!=, is, is not

a = 4
b = 2

# Lebih Besar Dari  > 
print('=================Lebih Besar Dari > ')
hasil = a > 3
print (a, '>', 3 , '=', hasil)
hasil = b > 3
print (b, '>', 3 , '=', hasil)
hasil = b > 2
print (b, '>', 2 , '=', hasil)
hasil = b >= 2
print (b, '>', 2 , '=', hasil)


# Lebih Besar Dari  <
print('=================Kurang Dari < ')
hasil = a < 3
print (a, '<', 3 , '=', hasil)
hasil = b < 3
print (b, '<', 3 , '=', hasil)
hasil = b < 2
print (b, '<', 2 , '=', hasil)

# Lebih Dari Sama Dengan  >=
print('=================Lebih Dari Sama Dengan >= ')
hasil = a >= 3
print (a, '>=', 3 , '=', hasil)
hasil = b >= 3
print (b, '>=', 3 , '=', hasil)
hasil = b >= 2
print (b, '>=', 2 , '=', hasil)

# Kurang Dari Sama Dengan  >=
print('=================Kurang Dari Sama Dengan <= ')
hasil = a <= 3
print (a, '<=', 3 , '=', hasil)
hasil = b <= 3
print (b, '<=', 3 , '=', hasil)
hasil = b <= 2
print (b, '<=', 2 , '=', hasil)

# Sama Dengan (==)
print('=================Sama Dengan == ')
hasil = a == 4
print (a, '==', 4 , '=', hasil)
hasil = b == 4
print (b, '==', 4 , '=', hasil)


# Tidak Sama Dengan (!=)
print('=================Tidak Sama Dengan != ')
hasil = a != 4
print (a, '!=', 4 , '=', hasil)
hasil = b != 4
print (b, '==', 4 , '=', hasil)


# 'Is' Sebagai Komparasi Object Identity

print('=================Object Identity "IS')
x = 5 # Ini adalah assignment membut object
y = 5
print('nilai x = ,',x,',id = ', hex(id(x)))
print('nilai y = ,',y,',id = ', hex(id(y)))

hasil = x is y 
print('x is y =', hasil)

x = 5 # Ini adalah assignment membut object
y = 6
print('nilai x = ,',x,',id = ', hex(id(x)))
print('nilai y = ,',y,',id = ', hex(id(y)))

hasil = x is y 
print('x is y =', hasil)

print('=================Object Identity "IS NOT')
x = 5 # Ini adalah assignment membut object
y = 5
print('nilai x = ,',x,',id = ', hex(id(x)))
print('nilai y = ,',y,',id = ', hex(id(y)))

hasil = x is not y 
print('x is y =', hasil)

x = 5 # Ini adalah assignment membut object
y = 6
print('nilai x = ,',x,',id = ', hex(id(x)))
print('nilai y = ,',y,',id = ', hex(id(y)))

hasil = x is not y 
print('x is y =', hasil)
