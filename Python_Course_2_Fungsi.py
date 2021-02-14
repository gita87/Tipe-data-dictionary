""""
Program menghitung luas segituga
"""

alas = 10
tinggi = 6

luas_segitiga = alas*tinggi / 2
print(f'segitiga dengan alas{alas} dan tinggi{tinggi} maka luasnya adalah {luas_segitiga}')

def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga

hitung_luas_segitiga(10, 6)
hitung_luas_segitiga(14, 9)

print(hitung_luas_segitiga(10, 6))
print(hitung_luas_segitiga(14, 9))
print()
print('Menghitung luas segita dengan fungsi = {hitung_luas_segitiga(10, 6)}')
print('Menghitung luas segita dengan fungsi = {hitung_luas_segitiga(14, 9)}')
print()
print(f'Menghitung luas segita dengan fungsi = {hitung_luas_segitiga(10, 6)}')
print(f'Menghitung luas segita dengan fungsi = {hitung_luas_segitiga(14, 9)}')
print()
ingin_cepat = True
if ingin_cepat :
    print('jalan mundur')
else :
    print('jalan lurus')

x = True
if x :
    print(1)
else :
    print(2)
