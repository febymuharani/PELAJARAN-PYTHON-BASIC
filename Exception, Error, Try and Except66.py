# Exception akan terjadi saat program mengalami 
# eror saat runtime

# contoh sederhana untuk menangkap exception

from math import nan

## contoh sederhana
#input_user = int(input("Masukkan angka: "))
#hasil = nan

#try:
#    hasil = 10/input_user
#except:
#    print("Input tidak boleh 0")

#print(f"Hasil = {hasil}")

## contoh di aplikasi

while(True):
    angka = int(input("Masukkan Angka Pembagi: "))
    try:
        hasil = 10/angka
        print(f"hasil = {hasil}")
        is_done = input("Lanjutkan? (y/n)")
        if is_done == "n":
            break
    except:
        print("pembagi nol, silahkan masukkan input lagi")

print("Akhir dari program 1")



#contoh aplikasi untuk membuat file data_66.txt
try:
    with open("data_66.txt",'r') as file:
        print(file.read())
except:
    print("data_66.txt tidak ditemukan, membuat file baru")
    with open("data_66.txt",'w',encoding='utf-8') as file:
        file.write("file baru")


print("akhir dari program 2")
