import json
import re

from songpy.music.chord import Chord
from songpy.song import OneChordAtom, SongPart, Song, SongLine
from songpy.utils import PolishNoteNamesPreprocessor
from songpy.utils.transpose import transpose_by_semitones

PREPROCESSORS_CHAIN = []


def register_preprocessor(preprocessor):
    PREPROCESSORS_CHAIN.append(preprocessor)


def preprocess_line(raw: str) -> str:
    product = raw
    for preprocessor in PREPROCESSORS_CHAIN:
        product = preprocessor.process(product)
    return product


def song_part_from_dictionary(dictionary: dict) -> SongPart:
    lines = list(map(parse_line, dictionary['content'].split('\n')))
    return SongPart(content=lines, type=dictionary['type'])


def parse_line(raw: str) -> [OneChordAtom]:
    product = preprocess_line(raw)
    pattern = r'(\[([^\]]*)\])?' + r'([^\[]*)'
    matches = re.finditer(pattern, product)
    return SongLine([OneChordAtom(text=match.group(3), chord=Chord.from_symbol(match.group(2)))
                     for match in matches][:-1])


def song_from_dictionary(dictionary: dict) -> Song:
    output = Song(dictionary['title'])
    output.lyrics_author = dictionary['lyrics']
    output.music_author = dictionary['music']
    # output.translation_author = dictionary['translated']
    content = dictionary['content']
    for song_part in content:
        output.add_song_part(song_part_from_dictionary(song_part))
    return output


class SimplePrinter:
    @staticmethod
    def print(song: Song) -> str:
        output = song.title
        for part in song.content:
            output += "\n"
            for line in part.content:
                output += "\n"
                output += line.lyrics() + " | " + " ".join(list(map(simple_printer, line.chords())))
        return output


def simple_printer(obj) -> str:
    return str(obj)


if __name__ == '__main__':
    register_preprocessor(PolishNoteNamesPreprocessor())
    file = open("song.json", 'r')
    song = json.load(file)
    file.close()
    song = song_from_dictionary(song)
    transpose_by_semitones(song, 8)
    print(SimplePrinter().print(song))
