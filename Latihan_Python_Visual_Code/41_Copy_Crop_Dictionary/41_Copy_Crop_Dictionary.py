# Copy Dictionary
print('\n')
teman_teman = {
    'cup' : 'ucup surucup',
    'tong' : 'otong surotong',
    'dung ': 'dudung surudung',
    'sep' :'asep si kasyep',
    'cuy' : 'ucu sirucuy'
}

friends = teman_teman.copy()
print(f'teman-teman : {teman_teman}\n')
print(f'friends : {friends}\n')

teman_teman['cup'] = 'ucup si kweren'
print(f'teman-teman : {teman_teman}\n')
print(f'friends : {friends}\n')


# Pop Dictionary 
dataAsep = friends.pop('sep')
print(f'Data Asep = {dataAsep}\n')
print(f'friends = {friends}\n')


# Popitem Dictionary
dataTerakhir = friends.popitem()
print(f'data terakhir = {dataTerakhir}\n')
print(f'friends = {friends}\n')










