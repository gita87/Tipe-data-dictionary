a, b, c, d, e = 'amin', 'budi', 'cici', 'dodi', 'egi'
print('sebelum pertukaran')
print(f'a={a}, b={b}, c={c}, d={d}, e={e}')
print('\nsetelah pertukaran')
a, b, c, d, e = 'egi', 'didi', 'cici', 'budi', 'amin'
print(f'a={a}, b={b}, c={c}, d={d}, e={e}')
""""


"""
# belajar kembali perulangan
daftar = [1, 2, 3]
for item in daftar:
    print(f'{item}')

for item in daftar:
    print(f'halo {item}')
daftar = [1, 2, 3]
print(f'{daftar[1]}')

ABG = ['noni', 'deko', 'jonan']
print(f'{ABG}')

("\n""\n")
print(f'\n{ABG[2]}')
print()
for item in ABG:
    print(f'{item}')
print()

print(f'\nhalo{ABG}')
for item in ABG:
    print(f' halo [item]')
    print(f'halo {item}')
print()

for item in range (0, len(ABG)):
    print(f'{item+1}. {ABG[item]} ')

print('test')
print()
mamalia = ['sapi', 'kambing', 'unta', 'zebra']
print(f'{mamalia}')
for item in mamalia :
    print(f'{item}')
print()

for item in range (0, len(mamalia)):
    print(f'{item+1}. {mamalia[item]}')
print()

hewan= [
    {'sapi' : 'bakso'},
    {'kambing' : 'kare'},
    {'unta' : 'goreng'},
    {'zebra' : 'tumis'}
]
print (f'{hewan}')
print()
for item in hewan :
    print (f'{item}')
print()
for item in range (0, len(hewan)):
    print (f'{item+1}. {hewan[item]}')
