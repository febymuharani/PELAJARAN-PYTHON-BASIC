# contoh membuat exception

from numbers import Number 


def tambah(a,b):
    if not isinstance(a,Number) or not isinstance(b,Number):
        raise "input harus angka"
    return a+b

print(tambah(5,5)) # akan jalan
#print(tambah(5,"v")) # tidak akan jalan


#angka = 0
#try:
#    hasil = 10/angka
#except Exception as eror_massage:
#    print(eror_massage)

angka = 0
try:
    hasil = 10/angka
except ZeroDivisionError as eror_massage:
    print(eror_massage)