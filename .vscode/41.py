# copy dictionary

teman_teman = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "sep":"asep sirasep",
    "dang":"dadang suradang"
}

friends = teman_teman.copy()

print(f"teman teman = {teman_teman}\n")
print(f"friend = {friends}\n")

teman_teman["cup"]= "ucup si keeren"
print(f"teman teman = {teman_teman}\n")
print(f"friend = {friends}\n")

# pop dictionary
dataAsep = friends.pop("sep")
print(f"data asep = {dataAsep}\n")
print(f"friends = {friends}\n")

# pop item dictionary
dataTerakhir = friends.popitem()
print(f"data terakhir = {dataTerakhir}\n")
print(f"friends = {friends}\n")