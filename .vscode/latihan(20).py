# Date and Time (latihan)

#import datetime as dt
#hari_ini = dt.date.today()
#print(hari_ini)
#print(f"hari ini adalah hari = {hari_ini:%A}")

#tanggal = dt.date(2006,2,27)
#print(tanggal)
#print(f"hari itu adalah hari = {tanggal:%A}")

import datetime as dt
print(" Silahkan masukkan \ntanggal, bulan dan tahun lahir anda \n")
tanggal = int(input("Tanggal \t: "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir anda adalah = {tanggal_lahir}")

hari_ini = dt.date.today()
print(f"Hari ini tanggal = {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30
sisa_hari_ultah = (umur_hari.days )
print(f"umur hari anda = {umur_hari}")
print(f"Hari lahir anda adalah = {tanggal_lahir:%A}")
print(f"Umur anda adalah = {umur_tahun} tahun {umur_bulan_sisa} bulan")
