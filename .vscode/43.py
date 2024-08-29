import datetime
import os



# template dict mahasiswa
mahasiswa_template = {
    'nama':'nama',
    'nim':'00000000',
    'sks_lulus':0,
    'lahir': datetime.datetime(1111,1,11)
}

data_mahasiswa = {}

os.system("cls") # Untuk windows
print(f"{'SELAMAT DATANG':^20}")
print(f"{'DATA MAHASISWA':^20}")
print("-"*20 )

mahasiswa = dict.fromkeys(mahasiswa_template.keys())
mahasiswa['nama'] = input("Nama Mahasiswa: ")
mahasiswa['nim']  = input("NIM Mahasaiswa: ")
mahasiswa['sks_lulus'] = int(input("SKS_lulus: "))
TAHUN_LAHIR = int(input("Tahun Lahir (YYYY): "))
BULAN_LAHIR = int(input("Bulan Lahir (1-12): "))
TANGGAL_LAHIR = int(input("TANGGAL LAHIR (1-31): "))
mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)
print(mahasiswa)
