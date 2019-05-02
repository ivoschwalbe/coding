class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(f"{line}")

happy_bday = Song(
    [
        "Happy birthday to you",
        "I don't want to get sued",
        "So I'll stop right there",
    ]
)

bulls_on_parade = Song(
    [
        "They rally around tha family",
        "With pockets full of shells",
    ]
)

ein_anderer_song = [
    "Fuchs du hast die Gans gestohlen,",
    "Gib sie wieder her,",
    "Gib sie wieder her,",
    "Sonst wird dich der Jäger holen,",
    "Mit dem Schießgewehr ..."
]

fuch_dhdGg = Song(ein_anderer_song)

happy_bday.sing_me_a_song()
print("# " * 10)
bulls_on_parade.sing_me_a_song()
print("# " * 10)
fuch_dhdGg.sing_me_a_song()