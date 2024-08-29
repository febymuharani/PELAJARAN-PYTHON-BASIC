#fahrenheit ke kelvin
print("\nFAHRENHEIT KE KELVIN\n")
fahrenheit = float(input('masukkan suhu dalam fahrenheit :'))
print("suhu adalah" ,fahrenheit, "fahrenheit")

celcius = ((5/9) * fahrenheit) - 32
kelvin = celcius + 273
print("suhu dalam kelvin" ,kelvin, "kelvin")

#kelvin ke fahrenheit
kelvin = float(input('masukkan suhu dalam kelvin :'))
print("suhu adalah" ,kelvin, "kelvin")

celcius = kelvin - 273
fahrenheit = ((9/5) * kelvin) + 32
print("suhu dalam fahrenheit" ,fahrenheit, "fahrenheit")