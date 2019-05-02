# Import das Modul argv aus dem Paket sys
from sys import argv

# argv ist ein Array mit erwarteten zwei Elementen
# argv[0] wird script zugewiesen
# argv[1] wird filename zugewiesen
# werden nicht genau 2 Parameter übergeben, gibt es einen Fehler
script, filename = argv

# Datei wird geöffet
# Standard: nur Lesen, Textd
# txt ist ein "file object"
# https://docs.python.org/3/library/functions.html#open
# https://docs.python.org/3/glossary.html#term-file-object
txt = open(filename)
# txt = open(argv[1])

# Der Dateiname wird ausgegeben
print(f"Here's your file {filename}:")

# in a wird der Text-Inhalt von txt gespeichert
a = txt.read()

# a (Textinhalt von txt von filename wird ausgegeben)
print(a)

# Schnack machen :)
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())