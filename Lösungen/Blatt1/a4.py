# Part (a)
length = input("Länge in Meter: ")
length = float(length)
print(f"Die Länge in Kilometern beträgt {length/1000}km")

# Part (b)
temp = input("Temperatur in Grad Celsius: ")
temp = float(temp)
temp = temp + 273.15
temp = int(temp * 100)/100  # my creative way to round to 2 figures
print(f"Die Temperatur in Grad Kelvin beträgt {temp}")

# Part (c)
length = input("Länge in Zentimeter: ")
length = float(length)
length = length/2.54
length = int(length*100)/100  # my creative way to round to 2 figures
print(f"Die Länge in Zoll beträgt {length}")

# Part (d)
temp = input("Temperatur in Grad Celsius: ")
temp = float(temp)
temp = 9/5 * temp + 32  # you find this conversion rule on Wikipedia
temp = int(temp * 100)/100  # my creative way to round to 2 figures
print(f"Die Temperatur in Grad Fahrenheit beträgt {temp}")


# Part (e)
FOOT_IN_METER = 0.3048  # By convention uppercase names are used for constants
INCH_IN_METER = 0.0254
length = input("Länge in Metern: ")
length = float(length)
# compute the whole feet contained in the length using integer division:
feet = length // FOOT_IN_METER
feet = int(feet)
# compute the remainder after deducting an integer number of feet
remainder = length % FOOT_IN_METER
inches = remainder / INCH_IN_METER  # convert the remainder to inches
inches = int(inches * 100)/100  # round creatively
print(f'{length} Meter entsprechedn {feet} ft. {inches}"')
