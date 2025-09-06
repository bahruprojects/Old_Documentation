# TYPE HINTS UNTUK FUNGSI
# BENTUK STANDAR FUNGSI

'''
def fungsi(parameter):
    print(parameter)
fungsi(1) 
fungsi('Ucup')
fungsi(True)
'''

'''
def fungsi(parameter):
    hasil = parameter**2
    print(parameter)
fungsi(1) 
fungsi('Ucup')
fungsi(True)
'''

# Penggunaan Type Hints
import string

def fungsi_dengan_hints(argument:int):
    """Fungsi Dengan Hints"""
    output = 10**argument
    return output
hasil = fungsi_dengan_hints(2) # Hanya Bisa int
print(hasil)

def display(argument:string):
    print(argument)
display('Ucup')
















