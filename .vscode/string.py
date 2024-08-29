data = "ini adalah string"
print(data)
print(type(data))

#1.Cara Membuat String
'''
1.Dengan menggukan single quote '...'
2.Dengan menggunaka double quotes "..."
'''
data = 'menggukanan single qoute'
print(data)

data = "menggunakan double qoute"
print(data)

print('"Halo Apa Kabar?"')
print("'Halo Apa Kabar?'")
print("ini adalah hari jum'at")


# 2.Menggunakan tanda (\)
# membuat tanda ' menjadi string (\')
print('mari sholat jum\'at') 
print('g\'day isn\'t it?')

# backlash (\\)
print("c:\\user\\ucup")

# tab (\t)
print("ucup\totong, jauhan")

# backspace (\b)
print("ucup \botong, deketan")

# newline (\n)
print("baris pertama.\nbaris kedua.") # LF -> line feed
print("baris pertama.\rbaris kedua.") # CR -> carriege return
print("baris pertama.\r\nbaris kedua.") # CRLF -> line feed carriege return -> windows

# 3. string literal atau raw

# hati-hati
print('C\new folder') # pathnya akan salah

# menggunakan raw string
print(r'c\new folder')

# multiline literal string
print('''
Nama  : ucup
kelas : 3SD
''')

# multiline literal string dan raw
print(r'''
Nama   : Ucup
Kelas  : 3SD\new 
Wesbite : www.ucup.com/newId
''') # jika memakai raw maka akan menjadi string atau kebaca
