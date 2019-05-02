#!/usr/bin/python3

days = "Montag Dienstag Mittwoch Donnerstag Freitag Samstag Sonntag 💁👌🎍😍"
months = "Jan\nFeb\nMär\nApr\nMai"

print(days)
print(months)

# Ok. Kontrollsequenzen scheinen ausgewertet zu werden.
# Ansonsten alles, wie eingegeben
lang = """

# >\n\t\n\nDas ist Text Zeile 1
Das ist Text Zeile 1
Das ist Tex\tt Zeile 1


Das ist Text Zeile 1
Das ist Text Zeile 1
Das ist Text Zeile 1
Das ist Text Zeile 1
Das ist Text Zeile 1

"""

print(lang)

# Noch einmal, ob ich auch nichts vergessen habe :(
print("Das ist {}, was man aber nicht sagen darf".format("Schei*e"))

# Ok. Auch das :)
print("Das ist {}, was man aber nicht sagen darf".format(lang))