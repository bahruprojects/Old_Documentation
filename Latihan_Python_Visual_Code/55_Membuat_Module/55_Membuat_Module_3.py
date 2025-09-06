# Module Matematika Dengan Import

from Modulematematika import tambah as add
from Modulematematika import kali as multiply
from Modulematematika import pangkat as exponen

import Modulematematika as Mod  # <--- Bisa Dilakukan 

hasil_tambah = add(1, 2, 3, 4, 5)
print(f'Hasil Tambah = {hasil_tambah}')

hasil_kali = multiply(1, 2, 3, 4, 5)
print(f'Hasil Kali = {hasil_kali}')

pangkat_3 = exponen(3)
print(f'Hasil Pangkat 3 = {pangkat_3(3)}')













