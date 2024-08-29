'''Type Hint Untuk Fungsi'''

# bentuk standar fungsi yang sudah kita pelajari

'''
STUDI KASUS
def fungsi(parameter):
    hasil = parameter**2
    print(hasil)


fungsi(1)
fungsi("ucup")
fungsi(True)
'''

# penggunaan type hints

import string

def sepuluh_pangkat(argumen:int) -> int:
    '''FUNGSI DENGAN HINTS'''
    output = 10**argumen
    return output

HASIL = sepuluh_pangkat(2)
print(HASIL)


def display(argumen:string):
    print(argumen)

display("ucup")