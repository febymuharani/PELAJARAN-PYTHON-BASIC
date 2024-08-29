# lambda function

def f_kuadrat(angka):
    return angka**2


print(f"hasil fungsi kuadrat = {f_kuadrat(3)}")


# kita coba dengan lambda
# output = lambda argument: expression
kuadrat = lambda angka : angka**2
print(f"hasil lambda kuadrat = {f_kuadrat(5)}")


pangkat = lambda num,pow : num**pow
print(f"Hasil Lambda pangkat = {pangkat(4,2)}")

## KEGUNAAN SI LAMBDA

# SORTING UNTUK LIST BIASA
data_list = ["aaaaaa","bbbb","ccc"]
data_list.sort()
print(f"sorted list = {data_list}")

# SORTING PAKE PANJANG
data_list.sort(key=len)
print(f"sorted list by len = {data_list}") # mengurutkan dari nama tersikit huruf nya
####/####
def panjang_nama(nama):
    return len(nama)

data_list.sort(key=panjang_nama)
print(f"sorted list by len = {data_list}") # hasilnya sama

### SORT PAKE LAMBDA
data_list = ["aaaaaa","bbbb","ccc"]
data_list.sort(key=lambda nama:len(nama))
print(f"sorted list by lambda = {data_list}") # hasilnya sama

# FILTER
data_angka = (1,2,3,4,5,6,7,8,9,10,11,12)

def kurang_dari_lima(angka):
    return angka < 5
data_angka_baru = list(filter(kurang_dari_lima,data_angka))
data_angka_baru = list(filter(lambda x:x<7,data_angka))
print(data_angka_baru)

# kasus genap
data_genap = list(filter(lambda x:(x%2==0),data_angka))
print(data_genap)

# kasus ganjil
data_ganjil = list(filter(lambda x:(x%2!=0),data_angka))
print(data_ganjil)

# kelipatan 3 
data_kelipatan = list(filter(lambda x:(x%3==0),data_angka))
print(data_kelipatan)

# ANONYMOUS FUNCTION
# currying <- Haskell Curry

def pangkat(angka,n):
    hasil = angka**n
    return hasil

data_hasil = pangkat(5,2)
print(f"Fungsi Biasa = {data_hasil}")

# menggunakan currying

def pangkat(n):
    return lambda angka:angka**n

pangkat2 = pangkat(2)
print(f"pangkat 2 = {pangkat2(5)}")

pangkat4 = pangkat(4)
print(f"pangkat 4 = {pangkat4(2)}")
print(f"pangkat bebas = {pangkat(4)(5)}") # nilai yang pertama pangkat & nilai yang kedua sebagai nilai yg akan di pangkat kan