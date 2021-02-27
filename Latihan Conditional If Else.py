jenis_kelamin = 'wanita'
umur = 28
asal = 'sumatera utara'

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
print()
if (jenis_kelamin == 'pria', umur == 30, asal == 'bali'):
    print(f'berbaris di sisi kanan lapangan, ambil posisi paling depan, sambil nari nari')
print()
if jenis_kelamin == 'pria' and umur >20 and umur <30 and asal == 'bali' :
    print ('berbaris di kanan lapangan, berbaris mengikuti dari belakang, sambil nari nari')
elif jenis_kelamin =='pria' and umur >30 and asal =='bali' :
    print('berbaris di kanan lapangan, ambil posisi paling depan, sambil nari nari')
elif jenis_kelamin == 'pria' and umur <20 and asal =='bali':
    print('berbaris di kanan lapangan, ambil posisi paling belakang, sambil nari nari')
elif jenis_kelamin == 'pria' and umur > 30 and asal == 'sumatera utara':
    print('berbaris di kanan lapangan, ambil posisi paling depan, sambil nyanyi')
elif jenis_kelamin == 'pria' and umur >20 and umur <30 and asal == 'sumatera utara' :
    print ('berbaris di kanan lapangan, berbaris mengikuti dari belakang, sambil nari nari')
elif jenis_kelamin == 'pria' and umur <20 and asal == 'sumatera utara' :
    print ('berbaris di kanan lapangan, berbaris paling belakang, sambil nyanyi')
elif jenis_kelamin == 'wanita' and umur >20 and umur <30 and asal == 'bali' :
    print ('berbaris di kiri lapangan, berbaris mengikuti dari belakang, sambil nari nari')
elif jenis_kelamin =='wanita' and umur >30 and asal =='bali' :
    print('berbaris di kiri lapangan, ambil posisi paling depan, sambil nari nari')
elif jenis_kelamin == 'wanita' and umur <20 and asal =='bali':
    print('berbaris di kiri lapangan, ambil posisi paling belakang, sambil nari nari')
elif jenis_kelamin == 'wanita' and umur > 30 and asal == 'sumatera utara':
    print('berbaris di kiri lapangan, ambil posisi paling depan, sambil nyanyi')
elif jenis_kelamin == 'wanita' and umur >20 and umur <30 and asal == 'sumatera utara' :
    print ('berbaris di kiri lapangan, berbaris mengikuti dari belakang, sambil nyanyi')
elif jenis_kelamin == 'wanita' and umur <20 and asal == 'sumatera utara' :
    print ('berbaris di kiri lapangan, berbaris paling belakang, sambil nyanyi')


print()
def sapa(nama):
    print("halo, " + nama +" apa kabar")

sapa('umar')