# LATIHAN LIST

# Program List Buku

list_buku = []

while True:
    print("\nMASUKKAN DATA BUKU")
    judul   = input("Masukkan Judul Buku\t: ")
    penulis = input("Masukkan Nama Penulis\t: ")

    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)
    

    print("\n\n","="*10,"DATA BUKU","="*10)
    for index,buku in enumerate(list_buku):
        print(f"{index} |{buku[0]} | {buku[1]}")


    print("\n\n","="*20)
    islanjut = input("Apakah Di Lanjutkan?(y/n) ")

    if islanjut == "n":
        break

print("PROGRAM SELESAI")