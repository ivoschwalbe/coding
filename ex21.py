def add(a, b):
  print(f"Adding {a} and {b}")
  return a + b

def substract(a, b):
  print(f"Substracting {a} and {b}")
  return a - b

def multiply(a, b):
  print(f"Multiplying {a} and {b}")
  return a * b

def divide(a, b):
  print(f"Dividing {a} and {b}")
  return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = substract(79, 5)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

print("Here is a puzzle.")
what = add(age, substract(height, multiply(weight, divide(iq, 2))))
print("That becomes: ", what, "Can you do it by hand?")