data_angka = [1,5,1,4,3,2,4,3,2,3,7,8,9,0]
print(f"data angka = \n{data_angka}")

# count data

jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3) 
print(f"jumlah angka 4 = {jumlah_data_4}")
print(f"jumlah angka 3 = {jumlah_data_3}")

# ambil posisi data 
data = ["Ucup","Otong","Ujeng","Asep"]
print(f"data = {data}")

# untuk mengambil index
index_ujeng = data.index("Ujeng")
print(f"index si ujeng = {index_ujeng}")
index_ucup = data.index("Ucup")
print(f"index si ucup = {index_ucup}")

# mengurutkan list
print(f"data angka sebelum sort = \n{data_angka}")
data_angka.sort()
print(f"data angka sort = \n{data_angka}")

print(f"data = {data}")
data.sort()
print(f"data sort = {data}")

# balik list 
data_angka.reverse()
print(f"data angka kebalikan = \n{data_angka}")

data.reverse()
print(f"data kebalikan = \n{data}")