import json

with open("countries.json", encoding="UTF-8") as file:
    countries = json.load(file)

for country in countries:
    print(f"{country['capital']} ist die Hauptstadt von {country['name']}")
