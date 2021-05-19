my_list = [4, 7, -12, 14, 28, 28, 4, 2, 1, -5, 18, 12]

# finde das Maximum
maximum = my_list[0]
for value in my_list:
    if value > maximum:
        maximum = value
print(f"Das Maximum ist {maximum}")

# Zusatz
# Erstelle eine neue Liste,
# in der das alte Maximum fehlt
# ggf. muss man es häufiger entfernen
new_list = my_list[:]
while maximum in new_list:
    new_list.remove(maximum)
second_maximum = new_list[0]

for value in new_list:
    if value > second_maximum:
        second_maximum = value
print(f"Der zweitgrößte Werte ist {second_maximum}")
