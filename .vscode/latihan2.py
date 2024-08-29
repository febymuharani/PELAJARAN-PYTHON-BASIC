 # episode latihan komperasi dan boolean

 # membuat gabugan area rentang dari angka

# ++++++3---------10++++++

inputUser = float(input("masukkan angka yang \nkurang dari 3 \natau \nlebih besar dari 10\n:"))

# ++++++++3-----------
# memeriksa angka yang kurang dari 3
isKurangDari = (inputUser < 3)
print("Kurang Dari 3 =", isKurangDari)


# ----------10++++++
# memeriksa angka yang lebih dari 10

isLebihDari = (inputUser > 10)
print("Lebih Dari 10 =", isLebihDari)


# ++++++3---------10++++++

isCorrect = isKurangDari or isLebihDari 
print("angka yang anda masukkan: ", isCorrect)

# ------3+++++++++10--------
# kasus irisan 
print("\n",10*"=","\n")
inputUser = float(input("masukkan angka yang \nlebih dari 3 \nand \nkurang dari 10\n:"))

#------3+++++++++
# LEBIH DARI 3
isLebihDari = (inputUser > 3)
print("Lebih Dari 3 =", isLebihDari)

#++++++10--------
# KURANG DARI 10
isKurangDari = (inputUser < 10)
print("Kurang Dari 10 =", isKurangDari)

# ------3+++++++++10--------
isCorrect = isLebihDari and isKurangDari
print("angka yang anda masukkan: ", isCorrect)



