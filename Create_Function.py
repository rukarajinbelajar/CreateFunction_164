def convert_temperature(value, unit):
    if unit.upper() == 'C':
        return (value * 9/5) + 32
    elif unit.upper () == 'F':
        return (value - 32) * 5/9
    else:
        print ("Unit harus 'C' atau 'F'")

input_suhu = int(input("Masukkan nilai suhu : "))
unit = input ("Masukkan satuan suhu ('C' untuk Celcius atau 'F' untuk Farenheit) : ")
convert_temperature(input_suhu, unit)
if unit.upper() == 'C':
    print(f"{input_suhu}°C = {convert_temperature(input_suhu, unit)}°F")
elif unit.upper() == 'F':
    print(f"{input_suhu}°C = {convert_temperature(input_suhu, unit)}°C")
else:
    print("Satuan tidak dikenal.")