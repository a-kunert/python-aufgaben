first_list = [2, 4, 5, 1, -23, 5, 9, 8]
second_list = [0, 8, -17, 4, 7, 9, 12]
# Initialisiere das Ergebnis als leere Liste
result = []

for value in first_list:
    if value in second_list:
        result.append(value)

print(f"Folgende Werte kommen in beiden Listen vor: {result}")