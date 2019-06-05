class MyStuff(object):
    def __init__(self, *args, **kwargs):
        print("Schnack")
        print(self)
        self.tangerine = "Ein Text, den ich nicht verstehe ..."
        return super().__init__(*args, **kwargs)
        

    def apple(self):
        print("Das druckt die Funktion im Object ...")

a = MyStuff()
a.apple()
print(a.tangerine)

# Klar geht das. Und zwar super :)
# Hahaha!
# Geht das?
# Und das?
# Und noch einmal