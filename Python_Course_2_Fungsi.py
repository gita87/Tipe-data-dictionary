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

def kilimanjaro ():
    print('gunung kilimanjaro')
kilimanjaro()

def arkand() :
    print('manutiras and the secret code of time')
arkand()

print()
def sapa_teman(nama):
    print("Hai", nama);
sapa_teman("Lisa")

def kinibalu(tinggi) :
    print('gunung kinibalu', tinggi)
kinibalu("2000 meter")

def menu(nama_makanan):
    print("tersedia,", (nama_makanan))
menu("jengkol")

def kucing(kesukaan):
    print("aktivitas kucing", (kesukaan))
kucing("tidur")
print()
def perhitungan_luas_segitiga(alas, tinggi):
    luas_segitiga = (alas * tinggi)/2
    print("Luas segituga adalah ", (luas_segitiga))
perhitungan_luas_segitiga(10, 3)
print()
def perhitungan_luas_persegipanjang(panjang, lebar) :
    luas_persegipanjang = (panjang*lebar)
    return luas_persegipanjang
    print("Luas persegi panjang adalah ", (luas_persegipanjang))
perhitungan_luas_persegipanjang(5,6)
def volume_balok(panjang, lebar, tinggi):
    volume = perhitungan_luas_persegipanjang(panjang, lebar)*tinggi
    print("volume balok adalah ", volume)
volume_balok(3,4,5)

print()
def sudut_segitiga(x,y):
    sudut = 180 - (x+y)
    print("luas sudut segitiga adalah ", sudut)
sudut_segitiga(90,40)
sudut_segitiga(30, 30)
print()
def menu_makanan(nama_makanan):
    print("menu makanannya adalah ", nama_makanan )
menu_makanan('bakso')
def rumus_lingkaran(z, r):
    lingkara = z*r
    print('luas lingkarannya adalah ', lingkara)
    return lingkara
rumus_lingkaran(2, 3.14)



