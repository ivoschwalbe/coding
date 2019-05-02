a = {
    "schnick": "schnack",
    "foo": "bar",
}

print(a)

b = a.copy()

print(a, b)

print(a.get("foo"))

# a.pop("foo")

print(a)

a[1] = "schnack123"

print("a" * 1000000)