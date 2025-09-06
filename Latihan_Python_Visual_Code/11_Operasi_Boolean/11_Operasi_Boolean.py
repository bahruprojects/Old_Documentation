# Operasi Logika / Boolean

# not, or, and, xor

print('===NOT===')
a = False
c = not a
print('data a  =', a)
print('data c =', c)



print('===OR===')
# JIka salah satu "True", Maka hasilnya 'True
a = False
b = False
c = a or b
print(a, 'OR', b, '=', c)
a = False
b = True
c = a or b
print(a, 'OR', b, '=', c)
a = True
b = False
c = a or b
print(a, 'OR', b, '=', c)
a = True
b = True
c = a or b
print(a, 'OR', b, '=', c)


print('===AND===')
# Jika kedua buah nilai "True", maka hasilnya "True"
a = False
b = False
c = a and b
print(a, 'and', b, '=', c)
a = False
b = True
c = a and b
print(a, 'and', b, '=', c)
a = True
b = False
c = a and b
print(a, 'and', b, '=', c)
a = True
b = True
c = a and b
print(a, 'and', b, '=', c)


print('===XOR===')
# Jika salah satu "True", maka hasilnya "True"
a = False
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)
a = False
b = True
c = a ^ b
print(a, 'XOR', b, '=', c)
a = True
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)
a = True
b = True
c = a ^ b
print(a, 'XOR', b, '=', c)











