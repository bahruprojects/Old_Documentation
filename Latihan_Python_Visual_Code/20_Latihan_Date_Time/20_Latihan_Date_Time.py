# Date & Time
print("\n")
import datetime as dt 

hari_ini = dt.date.today()
tanggal = dt.date(1997, 6, 18)

print(hari_ini)
print(tanggal)
print(f'hari ini adalah hari = {hari_ini:%A}')
print(f'hari ini adalah hari = {tanggal:%A}')

print('Silahkan masukkan tanggal. \nbulan tahun anda: \n ' )
tanggal = int(input('tanggal \t:'))
bulan = int(input('bulan \t\t:'))
tahun = int(input('tahun \t\t:'))


tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f'Tanggal Lahir Anda Adalah : {tanggal_lahir}')
print(f'Harinya adalah : {tanggal_lahir:%A}')


hari_ini = dt.date.today()
print(f'Hari Ini Adalah Tanggal : {hari_ini}')
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30
print(f'umur anda adalah : {umur_hari}')
print(f'umur anda adalah : {umur_tahun} tahun, {umur_bulan_sisa} bulan')












