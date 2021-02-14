jenis_kelamin = 'wanita'
umur = 24
asal = 'bali'

if (jenis_kelamin == 'pria') :
    print('berbaris di sisi kanan lapangan')
    if (umur > 25):
        print('ambil posisi paling depan')
        if (asal == 'bali'):
            print('sambil nari nari')
        elif (asal == 'sumatera utara'):
            print('nyanyi nyanyi')
    elif (umur >20 and umur <25):
        print('mengikuti dari belakang')
        if (asal == 'bali'):
            print('sambil nari nari')
        elif (asal == 'sumatera utara'):
            print('nyanyi nyanyi')
    elif (umur <20):
        print('berbaris paling belakang')
        if (asal == 'bali'):
            print('sambil nari nari')
        elif (asal == 'sumatera utara'):
            print('nyanyi nyanyi')

elif (jenis_kelamin == 'wanita') :
    print('berbaris di sisi kiri lapangan')
    if (umur > 25):
        print('berbaris paling depan')
        if (asal == 'bali'):
            print('sambil nari nari')
        elif (asal == 'sumatera utara'):
            print('nyanyi nyanyi')
    elif (umur > 20 and umur < 25):
        print('berbaris mengikuti dari belakng')
        if (asal == 'bali'):
            print('sambil nari nari')
        elif (asal == 'sumatera utara'):
            print('nyanyi nyanyi')
    elif (umur > 25):
        print('berbaris paling belakang')
        if (asal == 'bali'):
            print('sambil nari nari')
        elif (asal == 'sumatera utara'):
            print('nyanyi nyanyi')
