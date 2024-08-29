## TUTORAL MEMBACA FILE EKSTERNAL

print(3*"=", "Membaca file txt ", 3*"=")
file = open("Data.txt",mode="r")

print(f"status read : {file.readable()}")
print(f"status write : {file.writable()}")

## membaca seluruh file
print(file.read())

## membaca per baris
#print(file.readline(),end="") # membaca baris pertama
#print(file.readline(),end="") # membaca baris kedua

## baca semua baris sebgaai list
#print(file.readlines())

print(f"apakah file sudah di close : {file.closed}")
file.close()
print(f"apakah file sudah di close : {file.closed}")

## salah satu tehnik membuka file di pyhthon

print("\n",3*"=", "Membaca file txt denga with", 3*"=")
with open("data.txt",mode="r") as file:
    content = file.readline()
    print(content,end="")
    print(f"apakah file sudah di close : {file.closed}")

print(f"apakah file sudah di close : {file.closed}")