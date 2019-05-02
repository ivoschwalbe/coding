from sys import argv

# Kommandozeilenargumente parsen
script, input_file = argv

# Funktion: Gesamte Datei anzeigen
# Argument: Dateiobjekt
def print_all(f):
  print(f.read())

# Funktion "Zurückspulen"
# Argument: Dateihandle
# seek(0): zurück zu Zeile 0
def rewind(f):
  f.seek(0)

# Funktion eine Zeile anzeigen
# Argumente: Zeilennummer, Dateiobjekt
# Achtung: Die Zeilennummer dient nur der Ausgabe
# und hat nichts mit der angezeigten Zeile zu tun
def print_a_line(line_count, f):
  print(line_count, f.readline())

# Erst hier wird das Dateiobjekt erzeugt
# Vielleicht solle man das vor die Funktionen setzen?
current_file = open(input_file)

# Komplette Datei anzeigen
# einfach print(f.read())
print("First let's print the whole file:\n")
print_all(current_file)

# Zurückspulen der Datei zu Zeile 0
# rewind(f)
print("Now lets rewind, kind of like tape.")
rewind(current_file)

# Eine Zeile nach der anderen ausgeben
# f.readline()
print("Let's print three lines:\n")
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

print("name: " + current_file.name)
print("mode: " + current_file.mode)
print("encoding: " + current_file.encoding)
print("closed: " + str(current_file.closed))
print("errors: " + str(current_file.errors))
print("newlines: " + str(current_file.newlines))