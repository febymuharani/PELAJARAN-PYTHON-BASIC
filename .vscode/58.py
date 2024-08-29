import datetime

data_waktu = datetime.datetime.now()
print(f"waktu sekarang : {data_waktu}")
print(f"sekarang tahun : {data_waktu.year}")
print(f"hari ini hari : {data_waktu.strftime('%A')}")

from collections import Counter

data = ["a","b","a","c","a"]
#count = 0
#for i in data:
#    if i == "a":
#        count += 1
    
#print(count)


data_count = Counter(data)
print(f"data count = {data_count}")
print(f"data a = {data_count['a']}")


import io 

file = io.open("file_text.txt","r")
print(file.read())