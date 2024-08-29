data_0 = [1,2]
data_1 = [3,4]

data_list_biasa = [1,2,3,4]
print(f"list biasa = {data_list_biasa}")

list_2D = [data_0,data_1,6,7]
print(f"list 2D = {list_2D}")

# contoh penggunaan 
peserta_0 = ["Ucup",25,"Laki-Laki"]
peserta_1 = ["Otong",10,"Laki-Laki"]
peserta_2 = ["Dedeh",50,"Wanita"]

list_peserta = [peserta_0,peserta_1,peserta_2]
print(f"LIST PESERTA = \n{list_peserta}")

for peserta in list_peserta:
    print(f"nama\t: {peserta[0]}")
    print(f"umur\t: {peserta[1]}")
    print(f"Gender\t: {peserta[2]}\n")


# dengan reference
list_copy = list_peserta.copy();
print(f"LIST PESERTA = \n{list_copy}")
peserta_0[0] = "Michael"
print(f"LIST PESERTA = \n{list_copy}")
print(f"LIST PESERTA = \n{list_peserta}")