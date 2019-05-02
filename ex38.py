ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(" ")
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girls", "Boys"]

while len(stuff) != 10:
  next_one = more_stuff.pop()
  print("Adding: ", next_one)
  stuff.append(next_one)
  print(f"There we go: ", stuff)

print("Let's do some things wirh stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(" x ".join(stuff))
a = "xxx"
print(f' # {a} # '.join(stuff[1:5]))
