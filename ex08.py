#!/usr/bin/python3

# Keine Leerzeichen zwischen den {}
# Anzahl {} und Anzahl Dinge muss genau übereinstimmen
# In den {} kann noch viel Stuff stehen. Stay tuned!
formatter = "{} {} {} {}"
print(formatter.format(1, 2, 3, 4))
print(formatter.format("Hansi", "Birgit", "Franz", "Inge"))

print(formatter.format(True, False, True, False))
print(formatter.format(
  "hansi ist eine dumme Sau!",
  "Ohne Moos nix los!",
  "Das muss doch nicht sein!",
  "Und dann auch das noch!"
))

print(formatter)

# Oh dear!
print(formatter.format(formatter, formatter, formatter, formatter, ))