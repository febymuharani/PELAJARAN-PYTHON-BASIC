# SOAL DARI LATIHAN 2

#(1).(----0++++5----8++++11----)
#(2).(++++0----5++++8----11++++)

#(1).(----0++++5----8++++11----)
#(IRISAN)
inputUser = float(input("masukkan data:"))

angka1 = (inputUser > 0 and inputUser < 5)
print(angka1)

angka2 = (inputUser > 8 and inputUser < 11)
print(angka2)

isCorrect = angka1 or angka2
print("HASILNYA: ", isCorrect)

#(2).(++++0----5++++8----11++++)
#(GABUNGAN)
print("\n",10*"=","\n")
inputUser = float(input("masukkan data:"))

angka3 = (inputUser < 0 and inputUser > 5)
print(angka3)

angka4 = (inputUser < 8 and inputUser > 11)
print(angka4)

isCorrect = angka3 or angka4
print("HASILNYA: ", isCorrect)




