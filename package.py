import init 
from init.matematika import scientific
from init.matematika import basic

hasi_tambah = basic.tambah(5,5,5) # langsung name folder
print(f"hasil tambah = {hasi_tambah}")

hasil_fisika = init.fisika.gaya(20,20)
print(f"hasil = {hasil_fisika}")

hasil_kali = init.matematika.kali(2,5) # bisa masukkan nama folder dlu 
print(f"hasil kali = {hasil_kali}")

pangkat_3 = scientific.pangkat(3)
print(f"hasil pangkat = {pangkat_3(5)}")

#from init import *

#hasi_tambah = matematika.basic.tambah(5,5,5)
#print(f"hasil tambah = {hasi_tambah}")

#hasil_fisika = fisika.gaya(20,20)
#print(f"hasil = {hasil_fisika}")

#hasil_kali = matematika.basic.kali(2,5)
#print(f"hasil kali = {hasil_kali}")