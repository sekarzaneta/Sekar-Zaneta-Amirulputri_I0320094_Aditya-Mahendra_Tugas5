print("==== Menyapa Pengunjung Hotel ====")

nama = input('Masukkan Nama: ')
jenis_kelamin = input('Masukkan Jenis Kelamin (Laki laki/Perempuan): ')

if jenis_kelamin == 'Laki laki':
    print('Selamat datang, Mr', nama + '!')
else:
    print('Selamat datang, Mrs', nama + '!')
