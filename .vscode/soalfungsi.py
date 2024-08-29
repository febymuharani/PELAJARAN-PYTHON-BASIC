'''Latihan Fungsi'''

import os

# Program menghitung luas dan keliling persegi panjang

# Membuat header program


#os.system("cls")
#print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
#print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
#print(f"{'-'*40:^40}")

##Mengambil input user
#LEBAR = int(input("Masukkan Nilai Lebar: "))
#PANJANG = int(input("Masukkan Nilai Panjang: "))

##Program menghitung luas 
#LUAS = PANJANG*LEBAR
#KELILING = 2*(PANJANG+LEBAR)

##Tampilkan hasilnya
#print(f"hasil perhitungan luas = {LUAS}")
#print(f"hasil perhitungan keliling = {KELILING}")

def header():
    '''Fungsi Header'''
    os.system("cls")
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")


def input_user():
    '''Fungsi Input User'''
    lebar = int(input("Masukkan Nilai Lebar: "))
    panjang = int(input("Masukkan Nilai Panjang: "))

    return lebar,panjang


def hitung_luas(lebar,panjang):
    '''Fungsi Luas'''
    return lebar*panjang


def hitung_keliling(lebar,panjang):
    '''Fungsi Keliling'''
    return 2*(lebar+panjang)


def display(message,value):
    '''Fungsi Display'''
    print(f"hasil perhitungan{message} = {value}")

# Program Utamanya
while True:
    header()
    print("opsi perhitungan")
    print("1.menghitung luas")
    print("2.menghitung keliling")
    print("3.menghitung seluruhnya")

    opsi = input("pilih menu no: ")
    if opsi == "1":
        LEBAR,PANJANG = input_user()
        KELILING = hitung_keliling(LEBAR,PANJANG)
        display("keliling", KELILING)
    if opsi == "2":
        LEBAR,PANJANG = input_user()
        LUAS = hitung_luas(LEBAR,PANJANG)
        display("luas", LUAS)
    if opsi == "3":
        LEBAR,PANJANG = input_user()
        LUAS = hitung_luas(LEBAR,PANJANG)
        KELILING = hitung_keliling(LEBAR,PANJANG)
        display("luas", LUAS)
        display("keliling", KELILING)


    isContinue = input("apakah lanjut (y/n)? ")
    if isContinue == "n":
        break


print("Program Selesai, Terima Kasih")