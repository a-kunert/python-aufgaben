# Nutze die Funktion aus der letzten Aufgabe
def reverse_string(string):
    return string[::-1]


def is_palindrome(string):
    # Normiere die Eingabe, indem sie in Kleinbuchstaben
    # umgewandelt wird
    lowercase_string = string.lower()
    # Ein String ist genau dann ein Palindrom, wenn er mit
    # auch nach dem umdrehen mit sich übereinstimm
    return reverse_string(lowercase_string) == lowercase_string
