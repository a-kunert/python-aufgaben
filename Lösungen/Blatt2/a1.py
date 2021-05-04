x = input("X: ")
y = input("Y: ")
z = input("Z: ")

x = float(x)
y = float(y)
z = float(z)

median = 0

if x <= y <= z or z <= y <= x:
    median = y
elif x <= z <= y or y <= z <= x:
    median = z
else:
    median = x

print(f"Der Median ist {median}")
