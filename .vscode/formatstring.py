# format string

# contoh generic

# string
nama = "feby"
format_str = f"hello {nama}"
print(format_str)

# boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

# angka
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

# bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

# bilangan dengan ordo ribuan
angka = 2000
format_str = f"ribuan = {angka:,}"
print(format_str)

# bilangan decimal
angka = 2005.54321
format_str = f"desimal = {angka:.2f}"
print(format_str)

# penampilan leading zero
angka = 2005.54321
format_str = f"desimal = {angka:09.3f}"
print(format_str)

# menampilkan tanda +/-
angka_minus = -10
angka_plus  =  +10.1234
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+.2f}"
print(format_minus)
print(format_plus)

# memformat persen
persentase = 0.045
format_persen = f"persen = {persentase:.2%}"
print(format_persen)

# melakukan operasi aritmatika di dalam placeholder
harga = 10000
jumlah = 5
format_string = f"harga total = Rp{harga*jumlah:,}"
print(format_string)

# format angka lain binary, octal, hexal

angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)