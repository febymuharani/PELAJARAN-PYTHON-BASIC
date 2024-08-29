# operator dictionary

data_dict = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surudung"
}

# panjang dictionary
LENDICT = len(data_dict)
print(f"panjang dictionary: {LENDICT}") 

# mengecek key exist atau tidak
KEY = "cup"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data dict: {CHECKKEY}")

# mengakses value (read) dengan get
print(data_dict["cup"])
print(data_dict.get("cup"))
print(data_dict.get("kis","key tidak ditemukan")) # cek key dengan message (akan none atau tidak ada ditemukan)

# mengupdate data
data_dict["cup"] = "ucup si ganteng"
print(data_dict)

# menambah data
data_dict["sep"] = "asep surasep"
print(data_dict)

#/
data_dict.update({"cup":"ucup surucup"})
print(data_dict)
data_dict.update({"feby":"feby muharani"}) # kalau tidak ada maka dia akan menambah
print(data_dict)

# mendelate data pada dictionari
del data_dict["feby"]
print(data_dict)