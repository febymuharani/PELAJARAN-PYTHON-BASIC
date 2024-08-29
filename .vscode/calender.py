print ("|"+"="*28+"|")
print ("|"+"Program Menampilkan Calender"+"|")
print ("|"+"="*28+"|")

import calendar

tahun = int(input("Masukkan Tahun: "))
bulan = int(input("Masukkan Bulan: "))
print()

print("Hasil: ")
print(calendar.month(tahun,bulan))