# operator dan manipulasi string(2)
#  operator dalam bentuk method

## merubah case dari string

# merubah semua ke upper case
salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# merubah semua ke lower case
alay = "aKU keCe BanGeT"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

## pengecekan dengan menggunakan isX method
# contoh untuk pengecekan lower case
salam = "sist" 
apakah_lower = salam.islower() # hasilnya bool
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper() # hasilnya bool
print(salam + " is upper = " + str(apakah_upper))

# isalpha() <-- mengecek apakah semuanya huruf
# isalnum() <-- huruf dan angka
# isdecimal() <-- mengecek apakah semuanya angka
# isspace() <-- spasi, tab, newline \n
# istittle() <-- semua kata dimulai dengan huruf besar

judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle() # hasilnya bool
print(judul + " is title = " + str(cek_judul))

alpha = "CompanyX" # jangan di space
isaplha = alpha.isalpha()
print(alpha + " is alpha = " + str(isaplha))

num = "11111" 
isalnum = num.isalnum()
print(num + " is num = " + str(isalnum))

decimal = "105" 
isdecimal = decimal.isdecimal()
print(decimal + " is decimal = " + str(isdecimal))

space = "  " 
isspace = space.isspace()
print(space + " is space = " + str(isspace))

## ngecek komponen startswith() endwith()
cek_start = "Sangjangnim oppa".startswith("Sangjangnim")
print("start = " + str(cek_start))

cek_end = "Sangjangnim oppa".endswith("oppa")
print("end = " + str(cek_end))

## penggabungan komponen join() split()
pisah = ['aku','sayang','kamu']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = ' ehm '.join(pisah)
print(gabungan)

gabungan = "akuiyasayangehmkamu"
print(gabungan.split('ehm'))

## alokasi karakter rjust(), ljust(), center()
kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(20,"-")
print("'"+tengah+"'")

# kebalikannya -> strip()
tengah = tengah.strip("-") # menghilangkan tanda (-)
print("'"+tengah+"'")

kanan = kanan.strip() 
print("'"+kanan+"'")

