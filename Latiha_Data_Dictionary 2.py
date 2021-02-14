"""
DATA MANUSIA DAN HOBI
nama : budi, alan, jojo, malih
umur : 20, 23, 21, 24
hobi : ngegame, ngobrol, ngambul, ngentot
"""

print('HOBI MANUSIA')
hobi_dan_manusia = [{'nama' : 'budi', 'umur' : 20, 'hobi' : 'ngegame'},
                    {'nama' : 'alan', 'umur' : 23, 'hobi' : 'ngobrol'},
                    {'nama' : 'jojo', 'umur' : 21, 'hobi' : 'ngambul'},
                    {'nama' : 'malih', 'umur': 24, 'hobi' : 'ngopi'}]
print('side quest')
print()
print(hobi_dan_manusia)
print()
print(f'{hobi_dan_manusia}')
print()
print("print(f'{x}")
for x in hobi_dan_manusia:
    print(f'{x}')
print()
print("#FAIL CODE (F'[X]')   :")
for x in hobi_dan_manusia:
    print(f'[x]')
print()
# FAIL CODE for x in range (0, len(hobi_dan_manusia)) :
# FAIL CODE    print(f'{x}. {x[hobi_dan_manusia]}')
print("for x in range (0, len(hobi_dan_manusia))print(f'{x}. [x{hobi_dan_manusia}]'):")
for x in range (0, len(hobi_dan_manusia)):
    print(f'{x}. [x{hobi_dan_manusia}]')
print()
print("for x in range (0, len(hobi_dan_manusia)):(f'{x+1}. {hobi_dan_manusia[x]}') :")
for x in range (0, len(hobi_dan_manusia)):
    print(f'{x+1}. {hobi_dan_manusia[x]}')
print()
print("{hobi_dan_manusia [1]}:")
print(f"{hobi_dan_manusia [1]}")
print()
print("f{hobi_dan_manusia[1]['nama']} :")
print(f"{hobi_dan_manusia[1]['nama']}")
print(f"{hobi_dan_manusia[1]['nama']} {hobi_dan_manusia[1]['umur']}")
print()
print("f{hobi_dan_manusia[1]['nama'], "
      "hobi_dan_manusia [1]['umur'],"
      "hobi_dan_manusia [1]['hobi']} :")
print(f"{hobi_dan_manusia[1]['nama'],hobi_dan_manusia [1]['umur'],hobi_dan_manusia [1]['hobi']}")
print()
print("#FAIL CODE : f{hobi_dan_manusia[1]['nama']['umur']['hobi']} :")
#FAIL CODE print(f"{hobi_dan_manusia[1]['nama']['umur']['hobi']}")
print(f"{hobi_dan_manusia[1]['nama']} "
      f"{hobi_dan_manusia [1]['umur']} "
      f"{hobi_dan_manusia[1]['hobi']} ")
print()
print("#for r in range(0, len(hobi_dan_manusia)), {r+1}. {hobi_dan_manusia[r]} :")
#FAIL CODE for r in range(0, len(hobi_dan_manusia)):
#FAIL CODE    print(f"{r+1}. {hobi_dan_manusia[r]}")
print()
# FAIL CODE print("for r in range(0, len(hobi_dan_manusia)) {r+1}. {hobi_dan_manusia[r]} {hobi_dan_manusia}['nama']:")
#FAIL CODE for r in range(0, len(hobi_dan_manusia) ):
#FAIL CODE    print(f"{r+1}. {hobi_dan_manusia[r]} {hobi_dan_manusia}['nama']")
print()
#FAIL CODE for r in range (0, len(hobi_dan_manusia)):
#FAIL CODE    print(f"{r+1}. {hobi_dan_manusia[r]}")
print()
#FAIL CODE print("#for r in range(0, len(hobi_dan_manusia)), {r+1}. {hobi_dan_manusia[r]} :")
#FAIL CODE for r in range(0, len(hobi_dan_manusia)):
#FAIL CODE    print(f"{r+1}. {hobi_dan_manusia[r]}")
print()
print("for r in range(0, len(hobi_dan_manusia)) {r+1}. {hobi_dan_manusia[r]} {hobi_dan_manusia}['nama']:")
#FAIL CODE for r in range(0, len(hobi_dan_manusia) ):
#FAIL CODEprint(f"{r+1}. {hobi_dan_manusia[r]} {hobi_dan_manusia}['nama']")
print()
#FAIL CODE for r in range (0, len(hobi_dan_manusia)):
#FAIL CODE print(f"{r+1}. {hobi_dan_manusia[r]}")
print()

#FAIL CODE for r in(hobi_dan_manusia):
#FAIL CODE print(f"{r+1}nama {r['nama']}, umur {r['umur']}, hobi {r['umur']}")
#FAIL CODE for r in(hobi_dan_manusia):
#FAIL CODE print(f"{r+1}nama {r['nama']}, umur {r['umur']}, hobi {r['umur']}")
print()
#FAIL CODE for r in range(0,(hobi_dan_manusia)):
#FAIL CODE    print(f"{r+1}. nama{r['nama']}, umur{r['umur']}, hobi{r['hobi']} ")
#FAIL CODE for r in(hobi_dan_manusia):
#FAIL CODE    r in range (hobi_dan_manusia)
#FAI; CODE   print(f"nama {r['nama']}, umur {r['umur']}, hobi {r['umur']}")

x = [1,2,3]
for a in range (0, len(x)):
    print(f'{a+1}. {x[a]}')