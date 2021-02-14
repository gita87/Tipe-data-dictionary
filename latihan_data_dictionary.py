# data :
# sepatu : adidas
# ukuran : 33
# sepatu : nike
# ukuran : 34
# sepatu : bata
# ukuran : 35
# sepatu : air jordan
# ukuran : 36


print('Merek sepatu yang datang')
merek_sepatu_datang = {
    'ke_toko' : 'gepeto',
    'list_sepatu' : [{'sepatu' : 'adidas', 'ukuran': 33},
                     {'sepatu' : 'nike', 'ukuran' : 34},
                     {'sepatu' : 'bata', 'ukuran' : 35},
                     {'sepatu' : 'air jordan', 'ukuran' : 36}
    ]
}
print(f'{merek_sepatu_datang}')
print()
print(f"merek sepatu no. 1 adalah {merek_sepatu_datang['list_sepatu'][0]}")
print()
print(f"merek sepatu no 1 adalah {merek_sepatu_datang['list_sepatu'][0]['sepatu']}")
print()
# FAIL CODE print(f"{merek_sepatu_datang['list_sepatu'][2]['sepatu']} {'list_sepatu'[2]['ukuran']}")
# FAIL CODE print(f"{merek_sepatu_datang['list_sepatu']['list_sepatu'][2]}")
print(f"{merek_sepatu_datang ['list_sepatu'] [2] ['sepatu']}")
print()
# FAIL CODE print(f"{merek_sepatu_datang ['list_sepatu'] [1] ['sepatu'] ['ukuran']}")
print(f"{merek_sepatu_datang ['list_sepatu'][1]}")
print()
print(f"{merek_sepatu_datang ['list_sepatu'][1] ['sepatu']} {merek_sepatu_datang ['list_sepatu'][1] ['ukuran']}")
print()
# FAIL CODE print(f"{merek_sepatu_datang ['list_sepatu'][0,2] ['sepatu']} "
# FAIL CODE      f"{merek_sepatu_datang ['list_sepatu'][0,2] ['ukuran']}")
#FAIL CODE print(f"{merek_sepatu_datang ['list_sepatu']['sepatu']} "
#FAIL CODE     f"{merek_sepatu_datang ['list_sepatu']['ukuran']}")
print(f"{merek_sepatu_datang ['list_sepatu'][3] ['sepatu']} "
      f"{merek_sepatu_datang ['list_sepatu'][3] ['ukuran']}")
#FAIL CODE for item in range(0,len(merek_sepatu_datang)):
#FAIL CODE    print(f"{item} {item[merek_sepatu_datang ['list_sepatu']]}")
