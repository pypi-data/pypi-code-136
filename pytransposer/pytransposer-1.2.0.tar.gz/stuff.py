import re
with open('keys.txt', 'r') as f:
    chords = []
    for line in f.readlines():
        chord_line = re.findall(r'[^\⨪]+\-\>([^\n]+)', line)
        if chord_line:
            chord_line = chord_line[0]
            chords_in_line = chord_line.split()
            for chord in chords_in_line:
                chord = chord.strip('()')
                if chord not in chords:
                    chords.append(chord)
for ch in chords:
    print(ch)