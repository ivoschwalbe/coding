from sys import argv

script, filename = argv

print(f"We are going to erase {filename}.")
print("If you don't want that, hit ^C.")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file ...")
target = open(filename, "w")

print("Truncating the file ...")
target.truncate()

print("Done.\nNow I'm asking you three lines.")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm going to write these lines to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally: Close the file!")

target.close()

txt = open(filename)
content = txt.read()
print("Und jetzt die Ausfabe:\n")
print(content)