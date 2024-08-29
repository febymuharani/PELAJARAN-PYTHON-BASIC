# 1. Mode write


# akan otomatis membuat jika file tidak ada
# akan menimpa atau overwrite isinya
with open("data_1.txt","w",encoding="utf-8") as file:
    file.write("Otong surotong")


with open("data_1.txt","w",encoding="utf-8") as file:
    file.write("Ucup Surucup")

with open("data_1.txt","w",encoding="utf-8") as file:
    file.write("Overwrite")

# 2. mode append
with open("data_2.txt","w",encoding="utf-8") as file:
    file.write("Ucup Surucup\n")

with open("data_2.txt","a",encoding="utf-8") as file:
    file.write("Akan Nambah/tidak menimpa")

# 3.mode r+
with open("data_3.txt","w",encoding="utf-8") as file:
    file.write("Data ke 3\n")


with open("data_3.txt",'r+',encoding="utf-8") as file:
    file.write("baris-1\n")
    file.write("baris-2\n")
    file.write("baris-3\n")
    
with open("data_3.txt",'r+',encoding="utf-8") as file:
    data = file.read()
    print(data)

with open("data_3.txt",'r+',encoding="utf-8") as file:
    file.write("otong") # akan menimpa sesuai panjang data