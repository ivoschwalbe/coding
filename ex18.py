# this one is like your script with argv
def print_two(*args):
  arg1, arg2 = args
  print(f"arg1: {arg1}, arg2: {arg2}")
  print(args[0], args[1])

# ok, that *args is actually pointless, we just do this
def print_two_again(arg1, arg2):
  print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
  print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
  print("I got nothing!")

print_two("Zed", "Shaw")
print_two_again("Ivo", "Schwalbe")
print_one("Ivo")
print_none()
