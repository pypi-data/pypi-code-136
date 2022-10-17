class OneChordAtom:
    def __init__(self, text: str, chord):
        self.chord = chord
        self.text = text

    def transpose(self, interval):
        if self.chord is not None:
            self.chord = self.chord.transpose(interval)


class SongLine:
    def __init__(self, content: [OneChordAtom]):
        self.content = content

    def lyrics(self) -> str:
        return "".join([atom.text for atom in self.content])

    def chords(self):
        return [atom.chord for atom in self.content if atom.chord is not None]

    def formatted_chords(self, chord_printer):
        return " ".join([chord_printer(atom.chord) for atom in self.content if atom.chord is not None])

    def transpose(self, interval):
        for atom in self.content:
            atom.transpose(interval)


class SongPart:
    def __init__(self, content: [], type: str = 'verse'):
        self.content = content
        self.type = type

    def lyrics(self):
        return '\n'.join(self.lines())

    def lines(self):
        return [
            line.lyrics()
            for line in self.content
        ]

    def transpose(self, interval):
        for line in self.content:
            line.transpose(interval)


class Song:
    def __init__(self, title):
        self.title = title
        self.lyrics_author = None
        self.music_author = None
        self.translation_author = None
        self.content = []

    def add_song_part(self, songpart):
        self.content.append(songpart)

    def transpose(self, interval):
        for part in self.content:
            part.transpose(interval)


class SongBook:
    def __init__(self):
        self.songs = []

    def sort_songs(self):
        self.songs.sort(key=SongBook.compare_function)

    @staticmethod
    def compare_function(e):
        return e.title

    @staticmethod
    def from_dict(dictionary):
        output = SongBook()
        song_dicts = dictionary
        for dict in song_dicts:
            output.songs.append(Song.from_dict(dict))
        output.sort_songs()
        return output
