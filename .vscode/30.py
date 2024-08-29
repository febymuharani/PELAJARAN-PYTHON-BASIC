## Operasi

# index  0(-3)   1(-2)   2(-1)
data = ["Ucup","Otong","Dudung"]

# mengambil data dari list ini
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")

data_terakhir = data[-1]
print(f"data terakhir adalah = {data_terakhir}")

data_ucup = data[-3]
print(f"data ucup = {data_ucup}")

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

## Manipulasi data list

# menambahkan item pada list
print(f"data sebelum di tambah = \n{data}")
###data.insert(posisi,item)###
data.insert(0,"Asep")
print(f"data sesudah ditambh = \n{data}")


# ingin menambah di akhir list
data.append("jojon")
print(f"langsung masuk ke bagian paling akhir = \n{data}")

# menggabungkan list dengan list
data_baru = ["Meta","Feby","Ella","Riska"]
data.extend(data_baru)
print(f"data gabungan = \n{data}")

# merubah data
# kita ubah data 2 menjadi (nama lain)
data[2] = "Michael"
print(f"nama pun akan berubah = \n{data}")

# menghilangkan data
data.remove("Michael")
print(f"data remove = \n{data}")

# akan terjadi eror apabila list tidak sesuai di data

# meremove data paling belakang
data.pop()
print(f"data akhir akan ke remove = \n{data}")