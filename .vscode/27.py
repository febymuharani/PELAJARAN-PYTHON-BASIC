# BREAK

# EX 1
print("="*5+"CONTOH SATU"+"="*5)

angka = 0

while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}")
    if angka == 3:
        print("NICEEEE")
        break

    print("haaloo")

print("finiishh")


# EX 2
print("="*5+"CONTOH DUA"+"="*5)
data_int = int(input("hitung sampai = "))

angka = 0

while True:
    angka += 1
    print(f"feby -> {angka}")
    if angka == data_int:
        print("NICEEEE")
        break

    print("haaloo")


print("finiishh")

