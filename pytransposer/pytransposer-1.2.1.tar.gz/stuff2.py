import re
with open('keys.txt', 'r') as f:
    keys = {}
    for line in f.readlines():
        if 'maj' not in line and 'min' not in line:
            line = [c.strip('-> \n') for c in line.split('-')]
            if len(line) == 2:
                key = line[0]
                chords = line[1]
                chords = [c.strip('()') for c in chords.split()]
                keys[key] = chords
print(keys)