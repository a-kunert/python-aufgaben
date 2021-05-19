password = input("Welches Passwort möchtest Du verwenden?")

# Flags initialisieren
length_is_correct = 8 <= len(password) <= 20
contains_a_digit = False
contains_a_special_character = False
contains_no_forbidden_characters = False
contains_lowercase_letter = False
contains_uppercase_letter = False

# Alles durchchecken
for letter in password:
    # Achtung: Letter ist ein String
    if letter in ["0", "1", "2", "3", "4", "5", "6","7", "8", "9"]:
        contains_a_digit = True
    if letter in ["@", "!", "&", "?"]:
        contains_a_special_character = True
    if letter not in [" ", ".", ","]:
        contains_no_forbidden_characters = True
    if letter in "abcdefghijklmnopqrstuvwxyz":
        contains_lowercase_letter = True
    if letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        contains_uppercase_letter = True

if not length_is_correct:
    print("Das Passwort ist zu lang/zu kurz")
elif not contains_a_digit:
    print("Das Passwort muss eine Zahl enthalten")
elif not contains_a_special_character:
    print("Das Passwort muss ein Sonderzeichen (@!&?) enthalten")
elif not contains_no_forbidden_characters:
    print("Das Passwort darf kein Leerzeichen, Punkt oder Komma enhalten")
elif not contains_lowercase_letter:
    print("Das Passwort muss einen Kleinbuchstaben (a-z) enthalten")
elif not contains_uppercase_letter:
    print("Das Passwort muss einen Großbuchstaben (A-Z) enthalten")
else:
    print("Passwort akzeptiert")
