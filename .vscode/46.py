'''Fungsi Dengan Kembalian'''

# TEMPLATE FUNGSI DENGAN KEMBALIAN
# def nama_fungsi(argumen):
     # badan fungsi
     # return output

# fungsi(kuadrat)

def kuadrat(input_angka):
    '''Fungsi Kuadrat'''
    output_kuadrat = input_angka**2
    return output_kuadrat






y = kuadrat(5)
print(y)

print(kuadrat(6))

z = 10 + kuadrat(7)
print(z)

# fungsi tambah

def fungsi_tambah(angka_1,angka_2):
    '''Fungsi return dengan multi input'''
    return angka_1 + angka_2

a = fungsi_tambah(10,8)
print(a)

# fungsi dengan return banyak
 
def operasi_matematika(angka_1,angka_2):
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali   = angka_1 * angka_2
    bagi   = angka_1 / angka_2

    return tambah,kurang,kali,bagi


k,l,m,n = operasi_matematika(9,5)

 

print(f"Hasil Tambah = {k}")
print(f"Hasil Kurang = {l}")
print(f"Hasil Kali = {m}")
print(f"Hasil Bagi = {n}")


