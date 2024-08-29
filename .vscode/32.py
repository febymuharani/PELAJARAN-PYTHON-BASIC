## Teknik menduplikat list

a = ["Ucup","Otong","Ujeng","Asep"]
print(f"a = {a}")

b = a  # pass by reference
print(f"b = {b}")


# kita akan merubah member dari a

# ini akan merubah kedua list
a[1] = "Michael"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# address dari kedua list a dan b
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")

# mendupilkat list dengan copy

print("membuat list c dengan a.copy()")
c = a.copy() # full duplikat/data baru
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")


print("kita ubah data 1")
c[1] = "Dudung"
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("kita ubah data 3")
c[3] = "Tika"
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
