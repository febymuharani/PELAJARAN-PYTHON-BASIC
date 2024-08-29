'''DEFAULT ARGUMENT'''

# def fungsi(argument)
# def fungsi (argumen = nili defaultnya)


# CONTOH 1
def say_hello(nama = "Kamu"):
    '''fungsi dengan default argumen'''
    print(f"Halooo {nama}")

say_hello("feby")
say_hello()


# CONTOH 2
def sapa_dia(nama, pesan = "Apa Kabar? "):
    '''fungsi dengan satu input biasa dan satu default argumen'''
    print(f"HAII {nama}, {pesan}")


sapa_dia("FEBY","CANTIK YA HARI INI")
sapa_dia("otong")

# CONTOH 3
def hitung_pangkat(angka, pangkat):
    hasil = angka**pangkat
    return hasil

print(hitung_pangkat(2,4))


hasil = hitung_pangkat(pangkat=2, angka=5)
print(hasil) 

# CONTOH 4 

def fungsi(input1=1,input2=2,input3=3,input4=4):
     hasil = input1 + input2 + input3 + input4
     return hasil

print(fungsi())
print(fungsi(input3=10))