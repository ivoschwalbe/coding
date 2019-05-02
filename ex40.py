class Song(object):
    def __init__(self, lyrics, name):
        self.lyrics = lyrics
        self.name = name

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(f"{line}")

    def count_lines(self):
        print(f"{self.name} hat {len(self.lyrics)} Zeilen!")

happy_bday = Song(
    [
        "Happy birthday to you",
        "I don't want to get sued",
        "So I'll stop right there",
    ],
    "Happy Birthday"
)

bulls_on_parade = Song(
    [
        "They rally around tha family",
        "With pockets full of shells",
    ],
    "Bulls on parade"
)

ein_anderer_song = [
    "Fuchs du hast die Gans gestohlen,",
    "Gib sie wieder her,",
    "Gib sie wieder her,",
    "Sonst wird dich der Jäger holen,",
    "Mit dem Schießgewehr ..."
]

fuch_dhdGg = Song(ein_anderer_song, "Fuchs du hast die Gans gestohlen")

happy_bday.sing_me_a_song()
print("# " * 10)
bulls_on_parade.sing_me_a_song()
print("# " * 10)
fuch_dhdGg.sing_me_a_song()
print("# " * 10)
happy_bday.count_lines()
fuch_dhdGg.count_lines()
bulls_on_parade.count_lines()