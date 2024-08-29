# latihan loop
# latihan perulanga membuat segitiga

sisi = 10

# 1.mengguakan for

# dummy variabel
print("awal for")
count = 1
for i in range (sisi):
    print("*"*count)
    count += 1

print("akhir for")

# 2.menggunakan while
print("awal while")
count = 1
while True:
    print("*"*count)
    count += 1

    if count > sisi:
        break

print("akhir while")

# 3. hanya ganjil saja
print("awal while")
count = 1
while True:
  # print jika ganjil
    if (count%2):
        print("*"*count)
        count += 1
 # akan kembali ke atas jika ganjil
    else:
        count += 1
        continue


    # akan break jika count melebihi sisi
    if count > sisi:
        break

print("akhir while")

# 4. ex
print("awal while")
count = 1
spasi = 5
while True:
  # print jika ganjil
    if (count%2):
        print(" "*spasi, "+"*count)
        count += 1
 # akan kembali ke atas jika ganjil
    else:
        count += 1
        continue


    # akan break jika count melebihi sisi
    if count > sisi:
        break

print("akhir while")


# 4. segititga sama kaki ganjil
print("awal while")
count = 1
spasi = int(sisi/2)
while True:
  # print jika ganjil
    if (count%2):
        print(" "*spasi, "+"*count)
        spasi -= 1
        count += 1
 # akan kembali ke atas jika ganjil
    else:
        count += 1
        continue


    # akan break jika count melebihi sisi
    if count > sisi:
        break

print("akhir while")


#SOAL
# 5. ketupat
print("awal while")
count = 1
spasi = int(sisi/2)
while True:
  # print jika ganjil
    if (count%2):
        print(" "*spasi, "+"*count)
        spasi -= 1
        count += 1
 # akan kembali ke atas jika ganjil
    else:
        count += 1
        continue
    # akan break jika count melebihi sisi
    if count > sisi:
        break
while True:
    if (count%2):
        spasi += 1
        print(" "*spasi, "+"*count)
        count -= 1
    else:
        count -= 1
        continue
    if count == 0:
        break

print("akhir while")

