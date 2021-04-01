print("==== Mengkonversi Nilai ====")

nama = input('Masukkan Nama: ')
nilai = int(input('Masukkan Nilai: '))

if nilai < 60 and nilai >=0:
    nilai_akhir = "E"
elif nilai <= 64 and nilai >= 60:
    nilai_akhir = "C"
elif nilai <= 69 and nilai >= 65:
    nilai_akhir = "C+"
elif nilai <= 74 and nilai >= 70:
    nilai_akhir = "B"
elif nilai <= 79 and nilai >= 75:
    nilai_akhir = "B+"
elif nilai <= 84 and nilai >= 80:
    nilai_akhir = "A-"
elif nilai <= 100 and nilai >= 85:
    nilai_akhir = "A"
else:
    print("Maaf " + nama + ", nilai yang Anda masukkan tidak valid")

print("Halo, " + nama + "! Nilai Anda setelah dikonversi adalah", nilai_akhir)
