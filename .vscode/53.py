## GLOBAL DAN LOCAL SCOPE

nama_global = "otong" # <- disebut variabel global
kata1 = "hello world"

# akses variabel global dalam fungsi
def fungsi():
    print(f"fungsi menampilkan {nama_global}")

fungsi()


# akses variabel global dalam loop
for i in range(0,5):
    print(f"loop {i} - {nama_global}")


# akses variabel global dalam percabangan
if True:
    print(f"if menampilkan {nama_global}")


## variabel local scope

def fungsi2():
    nama_local = "Ucup" # <- variabel local scope (berada di dalam)

fungsi2()
#print(nama_local) # tidak bisa dilakukan

## Contoh 1.penggunaan akses variabel global scope

def say_otong():
    print(f"helo {nama}")

nama = "otong" # akan berjalan jika diletakka sebelum pemanggilan fungsi
say_otong()

## contoh 2. merubah variabel global
angka = 0
nama = "ucup"
def ubah(nilai_baru, nama_baru):
    global angka # fungsi ini mendapat akses merubah si angka
    angka = nilai_baru
    global nama # ambil dlu nama yang akan di akses
    nama = nama_baru # masukkan akses yang akan di ubah


#    angka = nilai_baru # tidak akan berjalan karena angka adalah local

print(f"sebelum {angka,nama}")
ubah(10,"rifki")
print(f"sesudah {angka,nama}")


angka = 0 

for i in range(0,5):
    angka += i
    angka_dummy = 0

print(angka)
print(angka_dummy)

if True:
    angka = 5
    angka_dummy = 10 

print(angka)
print(angka_dummy)


# hanya fungsi yang menggunakan global untuk merubah
# jika loop dan if bisa merubah atau mengaksess di dalam



