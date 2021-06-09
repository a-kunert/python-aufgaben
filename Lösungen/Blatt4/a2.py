def find_max(dictionary):
    # Finde das Maximum
    values = list(dictionary.values())
    # Bevor man mehr weiß,
    # ist der erste Wert das mögliche Maximum
    maximum = values[0]
    for value in values:
        # Ist ein Wert größer als das bisher größte
        # gefunde Element, wird dies das neue Maximum.
        if value > maximum:
            maximum = value
    # Wenn man das Maximum kennt,
    # finde alle Schlüssel, wo das Maximum
    # angenommen wird.
    result = []
    for key, value in dictionary.items():
        if value == maximum:
            result.append(key)
    return result
