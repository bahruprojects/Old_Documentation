
# TUGAS 
# Rumus Fahrenheit Ke Kelvin
# Kelvin Ke Fahrenheit


# Fahrenheit Ke Kelvin 
fahrenheit = float(input('Masukkan Nilai Fahrenheit :  '))
print('Suhu Dalam Fahrenheit Adalah  ', fahrenheit, 'F')
kelvin = (5/9)*(fahrenheit - 32) + 273
print('Suhu Dalam Kelvin Adalah  ', kelvin, 'k')

# Kelvin Ke Fahrenheit
kelvin = float(input('Masukkan Nilai kelvin :  '))
print('Suhu Dalam Kelvin Adalah  ', kelvin, 'k')
fahrenheit = ((9/5) * (kelvin - 273)) + 32
print('Suhu Dalam Fahrenheit Adalah  ', fahrenheit, 'F')
