a = 25
print('nilai dari a adalah', a)

nama = 'joni'
print('nama saya adalah', nama)

def salam ():
    print ("selamat pagi")
salam()

def sapa(nama):
    print("Hi, " + nama + ". Apa kabar?")
sapa('umar')

#FAIL CODE def sapa(nama):
#FAIL CODE     print("Hi", + nama + ". Apa kabar?")
#FAIL CODE sapa ('umar')
#CAUSE : tanda koma pada line 16 berada di luar tanda kutip dari kata Hi >> "Hi",
#THE RIGHT ONE : "Hi,"

def menu_buah(jenis_buah):
    print("ada buah : "  +jenis_buah)

menu_buah('semangka')
menu_buah('apel')
menu_buah('jeruk')


def scaramble_egg() :
    print ("telor dadar")
scaramble_egg()
print()

def gelas (jenis_kopi):
    print('kopi '+jenis_kopi)
gelas ('gayo')
gelas ('pea berry')

def makan(jenis_masakan) :
    print('pengen makan '+jenis_masakan)
makan ('nasi goreng pete')
makan ('mie ayam')
makan ('capcay')

foo = {"kegiatan": "Belajar Python",
       "website": "Duniailkom",
       "hasil": "Yakin bisa!"}

print(foo["website"])

flow = {1: "round", 2: "forsaken", 3 : "karashima"}
print(f'{flow[1]} {flow[2]} {flow[3]}')

for x in range (0, len(flow)):
    print(f"{x+1} [x{flow}]")
#FAIL CODE for x in range (0, (flow)):
#FAIL CODE    print(f"{x+1} {flow}")
print()
#FAIL CODE Troll = [1]: "round", 2: "forsaken", 3 : "karashima"]
rex = {"nemo": "round", "vlor": "forsaken", "strike": "karashima"}
for item in rex:
    print(item)
print()
for item in rex:
    print({item})
print()
#FAIL CODE for item in rex:
#FAIL CODE    print(item{rex})
#fAIL CODE for item in rex :
#FAIL CODE    print(rex{item})
for item in rex :
    print(f'rex{item}')
for d in range(0, len(rex)) :
    print (f"{d+1} {rex}")
for d in range(0, len(rex)):
    print(f"{d+1} {rex}")

