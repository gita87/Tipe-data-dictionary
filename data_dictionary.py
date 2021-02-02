"""

Belajar penggunaan data dictionary tanggal 29 January 2021

"""

# kamus data dictionary adalah : {}
# data dictionary untuk menghubungkan key ke value

kamus_ind_eng = {'anak': 'son', 'istri': 'ibu', 'suami': 'husband'}

print()
print(kamus_ind_eng['anak'])
print()
print(kamus_ind_eng['istri'])
print()
print(kamus_ind_eng['suami'])
print()

print('data ini dikirmkan oleh Server Gojek, untuk memberikan info driver di sekitar pemakai aplikasi')
data_dari_server_Gojek = {
    'tanggal': '2020-06-10',
    'driver_list': [
        {'nama': 'eko', 'jarak': 10},
        {'nama': 'dwi', 'jarak': 30},
        {'nama': 'tri', 'jarak': 100},
        {'nama': 'catur', 'jarak': 200}
    ]
}

print(data_dari_server_Gojek)
print(f"driver di sekitar sini {data_dari_server_Gojek['driver_list']}")
print(f"driver #1 {data_dari_server_Gojek['driver_list'][0]}")
print(f"driver #3 {data_dari_server_Gojek['driver_list'][3]}")
print()
print(f"Jarak driver terdekat {data_dari_server_Gojek['driver_list'][0]['jarak']} meter")
print(f"Driver Gojek terjauh adalah {data_dari_server_Gojek['driver_list'][3]['nama']}")
print()
print(f"coba dulu {data_dari_server_Gojek['driver_list'][2]['nama']}")
print(f"Driver {data_dari_server_Gojek['driver_list'][2]['nama']} berjarak "
      f"{data_dari_server_Gojek['driver_list'][2]['jarak']} meter")
