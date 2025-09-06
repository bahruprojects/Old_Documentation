import time 


import Sains.Matematikaa # Sains Adalah Package, Matematikaa Adalah Module
from Sains import Fisika
from Sains.Fisika import gaya as force


t_start = time.time()

hasil_tambah = Sains.Matematikaa.tambah(1, 2, 3, 4, 5, 6)
print(f'Hasil Tambah Adalah = {hasil_tambah}')

gaya = Fisika.gaya(90, 10)
print(f'Gaya Adalah = {gaya}')

gaya = force(90, 10)
print(f'Gaya Adalah = {gaya}')


t_end = time.time()
print(f'Waktu Eksekusi Adalah = {t_end - t_start}')




















