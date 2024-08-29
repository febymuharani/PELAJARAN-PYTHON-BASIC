# Import statement
# import berfungsi mengambil program dari file eksternal .py (program dari luar yang sudah ada/sudah di buat)


# 1.menyambung program
import program_feby # akan berjalan sesuai yang ada d file program_feby

# 2.import dengan data
import data1 # <- namafile
import data2

# nama data yang ada di namafile
#print(data) # akan eror
print(data1.data) # masukan dlu namafile baru masukkan nama data yang ada di dalam nya maka akan berjalan
print(data2.data) # akan berjalan walaupun nama data sama tetapi berada di nama file yang berbeda

# 3.import dengan fungsi
import datamat

hasil = datamat.tambah(5,5)
print(hasil)

# jika mengimport fungsi masukkan namafile lalu buat data masukkan namafile.fungsi(yang akan di akses) maka akan berjalan