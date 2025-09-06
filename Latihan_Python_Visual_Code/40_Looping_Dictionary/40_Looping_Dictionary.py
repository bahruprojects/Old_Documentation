# Looping Dictionary

teman_teman = {
    'cup' : 'ucu surucup',
    'tong' : 'otong surotong',
    'dung' : 'dudung surudung',
    'sep' : 'asep si kasyep',
    'cuy' : 'ucuy surucuy'
}

# Looping First Try

for teman in teman_teman:
    print(teman) # Yang Keluar Adalah Key-nya

# Operator Untuk Mengambil Item / Iterables
keys = teman_teman.keys()
print(keys)

for key in teman_teman.keys():
    print(teman_teman.get(key))

values = teman_teman.values()
print(values)

for value in teman_teman.values():
    print(value)

items = teman_teman.items()
print(items)

for item in teman_teman.items():
    print(item)

for key, value in teman_teman.items():
    print(f'Key = {key}, value = {value}')





































