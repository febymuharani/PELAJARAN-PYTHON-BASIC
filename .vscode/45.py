'''Fungsi dengan Argumen (input)'''

# TEMPLATE
# def nama_fugsi(argumen):
    # badan fungsi

def hello_world(nama):
    '''fungsi hello world menerima input dengan variabel nama'''
    print(f"Silahkan Masuk Kepada {nama}")

hello_world("ucup")
hello_world("asep")

# program tambahan

def tambah(angka_1,angka_2):
    '''fungsi tambah'''
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")

tambah(1,5)
tambah(10,5)

def say_hi(list_peserta):
    '''fungsi say hi'''
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
         print(f"Yang Terhormat {peserta}")

anggota_boyband = ["Ucup","Otong","Asep"]

say_hi(anggota_boyband)