#!/usr/bin/python3

print("Mary had a little lamb.")
print("Its fleece was white as {}.".format("snow"))
print("And everywhere that Mary went.")
print("." * 10)

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# end = "bestimmt das Ende des Strings"
# sep = "bestimmt den String zwischen den Strings"
  # aber nur bei Verknüpfung mit ","
print(end1 + end2 + end3 + end4 + end5 + end6, end = " ")
print(end7 + end8 + end9 + end10 + end11 + end12)


# C -- h -- e -- e -- s -- e oo Burger
print(end1, end2, end3, end4, end5, end6, sep = " -- ", end = " oo ")
print(end7 + end8 + end9 + end10 + end11 + end12)

