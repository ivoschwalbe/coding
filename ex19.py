def cheese_and_crackers(cheese_count, box_of_crackers):
  print(f"You have {cheese_count}, cheeses!")
  print(f"You have {box_of_crackers} boxes of crackers!")
  print("- - - - - - - - - - - - - - - - ")
#   print("Man that's enough for a party!")
#   print("Get a blanket.\n")



print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("Or, we can use variables from our script:")

amount_of_cheese = int(input("Cheese: "))
amount_of_crackers = int(input("Crackers: "))

# amount_of_cheese = 10
# amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even math inside too:")
cheese_and_crackers(10 + amount_of_cheese, 300 * amount_of_crackers)

print("And we can combine the two, variables an math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
