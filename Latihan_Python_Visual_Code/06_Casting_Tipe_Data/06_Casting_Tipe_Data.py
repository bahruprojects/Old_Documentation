# Casting = Merubah Tipe Data Ke Tipe Lain
# Tipe Data = int, float, str, bool

## INTEGER
data_int = 9
print('data = ', data_int, ', type = ', type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # Akan 'False' jika nilai 0, dan 'True' jika nilai 1 
print('data = ', data_float, ', type = ', type(data_float))
print('data = ', data_str, ', type = ', type(data_str))
print('data = ', data_bool, ', type = ', type(data_bool))

print('############################################################')

## FLOAT
data_float = 9.5
print('data = ', data_float, ', type = ', type(data_float))

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float) # Akan 'False' jika nilai 0, dan 'True' jika nilai 1 
print('data = ', data_int, ', type = ', type(data_int))
print('data = ', data_str, ', type = ', type(data_str))
print('data = ', data_bool, ', type = ', type(data_bool))

print('############################################################')

## BOOLEAN
data_bool = True
print('data = ', data_bool, ', type = ', type(data_bool))

data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool) # Akan 'False' jika nilai 0, dan 'True' jika nilai 1 
print('data = ', data_int, ', type = ', type(data_int))
print('data = ', data_str, ', type = ', type(data_str))
print('data = ', data_float, ', type = ', type(data_float))

print('############################################################')

## String
data_str = '20'
print('data = ', data_str, ', type = ', type(data_str))

data_int = int(data_str)
data_bool = bool(data_str)
data_float = float(data_str) # Akan 'False' jika nilai 0, dan 'True' jika nilai 1 
print('data = ', data_int, ', type = ', type(data_int))
print('data = ', data_bool, ', type = ', type(data_bool))
print('data = ', data_float, ', type = ', type(data_float))

