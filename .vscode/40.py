# Looping dictionary

teman_teman = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "sep":"asep sirasep",
    "dang":"dadang suradang"
}

# looping first try(yang keluar akan key nya)
for teman in teman_teman:
    print(teman)

# operator untuk mengambil item / iterables
print("="*10)
keys = teman_teman.keys()
print(keys)

for key in teman_teman.keys():
    print(teman_teman.get(key))

print("="*10)
values = teman_teman.values()
print(values)

for values in teman_teman.values():
    print(values)

print("="*10)
items = teman_teman.items()
print(items)

for items in teman_teman.items():
    print(items)

print("="*10)
for key,values in teman_teman.items():
    print(f"key = {key}, value = {values}")