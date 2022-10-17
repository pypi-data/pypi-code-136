from songpy.music import Interval, Note
from songpy.music.chord import Chord
from songpy.song import Song

PREFERRED_ENHARMONY = {
    Chord.Mode.MINOR: [
        "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "Bb", "B"
    ],
    Chord.Mode.MAJOR: [
        "C", "Db", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"
    ]
}


def transpose_by_semitones(song: Song, semitones: int):
    semitones = semitones % 12
    if semitones == 0:
        return song
    first_chord = find_first_chord(song)
    if first_chord is None:
        return song
    interval = preferred_interval(first_chord, semitones)
    song.transpose(interval)



def find_first_chord(song: Song):
    for part in song.content:
        for line in part.content:
            for atom in line.content:
                if atom.chord is not None:
                    return atom.chord
    return None


def distance_from_c(note: Note) -> int:
    return Interval.between(Note.from_symbol("C"), note).semitones()


def preferred_interval(initial_chord: Chord, semitones: int) -> Interval:
    semitones_from_c = (distance_from_c(initial_chord.root()) + semitones) % 12
    return Interval.between(initial_chord.root(),
                            Note.from_symbol(PREFERRED_ENHARMONY[initial_chord.mode()][semitones_from_c]))
