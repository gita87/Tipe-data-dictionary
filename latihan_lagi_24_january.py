print('hello boy')
print('___' * 8)

print('\nbelajar percabangan')

ingin_cepat = True
if ingin_cepat:
    print('\njalan lurus')
else:
    print('jalan mundur')

print('\ntest lagi')

main_game = False
if main_game:
    print('\n libur')
else:
    print('\n masuk kerja')

print('\n coba lagi')

istri_2 = False
if istri_2:
    print('\nnafsu')
else:
    print('\nmata keranjang')
print('\nbelajar perulangan')

jumlah_anak = 10
for index_anak in range(2, jumlah_anak + 3):
    print(f'halo anak {index_anak}')

menu_makanan = ['nasi goreng', 'gado-gado', 'pete', 'lemper', 'bakso']
print(len(menu_makanan))

luas = [10, 15, 20, 25, 30, 35, 50]
print(min(luas))
print()
angka = [12, 56, 34, 10, 45]
angka.sort()
print(angka)

print()
r = {'lemon': 'kagura', 'R7': 'chou', 'tuturu': 'bart', 'albert': 'cloude'}
print(r)

k = {'xinn': 'ling'}
print(k)
print()
r.update(k)
print(r)
print()
T = {2, 4, 5, 7}
print(T)
X = {8}
print(X)
X.update(T)
print(X)

