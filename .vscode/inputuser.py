# menginput data ke user

# apapun yang di masukin maka tipe data adalah string
data = input("masukkan data: ")
print("data = ",data,",type =",type(data))
#jika kita ingin mengambil int, maka
angka = float(input("masukkan angka: "))
angka = int(input("masukkan angka: "))
print("data = ",angka,",type =",type(angka))  

# bagaimana dengan boolean
biner = bool(int(input("masukkan nilai boolean: ")))
print("data = ",biner,",type =",type(biner))  