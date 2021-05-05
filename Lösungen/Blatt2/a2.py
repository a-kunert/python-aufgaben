for k in range(1, 101):
    name = ""
    # Durch den folgenden Weg spart man sich ein Conditional
    # für den Fall, dass k durch 15 teilbar ist.
    if k % 3 == 0:
        name = name + "Fizz"
    if k % 5 == 0:
        name = name + "Buzz"
    # Ah man muss auch noch prüfen, ob man ein Wort oder die Zahl ausgibt
    # Daher klappt es leider doch nicht mit nur 2 Conditionals
    if name:
        print(name)
    else:
        print(k)
