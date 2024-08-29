# latihan membuat Kalkulator sederhana

print(20*"=")
print("Kalkulator Sederhana")
print(20*"=" + "\n")

angka_1 = float(input("Masukkan Angka 1 = "))
operator = (input("Operator (+,-,*,/) : "))
angka_2 = float(input("Masukkan Angka 2 = "))

# Percabangan nya

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"Hasilnya adalah {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"Hasilnya adalah {hasil}")
elif operator == "*":
    hasil = angka_1 * angka_2
    print(f"Hasilnya adalah {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"Hasilnya adalah {hasil}")
else:
    print("SALAH BRO")

print("Akhir dari program,terima kasih!")
