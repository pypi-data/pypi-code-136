from src.pytransposer.transposer import express_chord_in_key, config
express_chord_in_key('SI', 'Db', 'doremi')

a = {'C': ['C', 'C'+config.sharp, 'D', 'E'+config.flat, 'E', 'F', 'F'+config.sharp, 'G', 'A'+config.flat, 'A', 'B'+config.flat, 'B'],
			'C'+config.sharp: ['B'+config.sharp, 'C'+config.sharp, 'D', 'D'+config.sharp, 'E', 'E'+config.sharp, 'F'+config.sharp, 'G', 'G'+config.sharp, 'A', 'A'+config.sharp, 'B'],
			'D'+config.flat: ['C', 'D'+config.flat, 'D', 'E'+config.flat, 'F'+config.flat, 'F', 'G'+config.flat, 'G', 'A'+config.flat, 'B'+config.flat+config.flat, 'B'+config.flat, 'C'+config.flat],
			'D': ['C', 'C'+config.sharp, 'D', 'E'+config.flat, 'E', 'F', 'F'+config.sharp, 'G', 'G'+config.sharp, 'A', 'B'+config.flat, 'B'],
			'D'+config.sharp: ['B'+config.sharp, 'C'+config.sharp, 'C'+config.sharp+config.sharp, 'D'+config.sharp, 'E', 'E'+config.sharp, 'F'+config.sharp, 'F'+config.sharp+config.sharp, 'G'+config.sharp, 'A', 'A'+config.sharp, 'B'],
			'E'+config.flat: ['C', 'D'+config.flat, 'D', 'E'+config.flat, 'E', 'F', 'G'+config.flat, 'G', 'A'+config.flat, 'A', 'B'+config.flat, 'C'+config.flat],
			'E': ['C', 'C'+config.sharp, 'D', 'D'+config.sharp, 'E', 'F', 'F'+config.sharp, 'G', 'G'+config.sharp, 'A', 'B'+config.flat, 'B'],
			'F': ['C', 'D'+config.flat, 'D', 'E'+config.flat, 'E', 'F', 'F'+config.sharp, 'G', 'A'+config.flat, 'A', 'B'+config.flat, 'B'],
			'F'+config.sharp: ['C', 'C'+config.sharp, 'D', 'D'+config.sharp, 'E', 'E'+config.sharp, 'F'+config.sharp, 'G', 'G'+config.sharp, 'A', 'A'+config.sharp, 'B'],
			'G'+config.flat: ['C', 'D'+config.flat, 'E'+config.flat+config.flat, 'E'+config.flat, 'F'+config.flat, 'F', 'G'+config.flat, 'G', 'A'+config.flat, 'B'+config.flat+config.flat, 'B'+config.flat, 'C'+config.flat],
			'G': ['C', 'C'+config.sharp, 'D', 'E'+config.flat, 'E', 'F', 'F'+config.sharp, 'G', 'G'+config.sharp, 'A', 'B'+config.flat, 'B'],
			'G'+config.sharp: ['B'+config.sharp, 'C'+config.sharp, 'D', 'D'+config.sharp, 'E', 'E'+config.sharp, 'F'+config.sharp,'F'+config.sharp+config.sharp, 'G'+config.sharp, 'A', 'A'+config.sharp, 'B'],
			'A'+config.flat: ['C', 'D'+config.flat, 'D', 'E'+config.flat, 'F'+config.flat, 'F', 'G'+config.flat, 'G', 'A'+config.flat, 'A', 'B'+config.flat, 'C'+config.flat],
			'A': ['C', 'C'+config.sharp, 'D', 'D'+config.sharp, 'E', 'F', 'F'+config.sharp, 'G', 'G'+config.sharp, 'A', 'A'+config.sharp, 'B'],
			'A'+config.sharp: ['B'+config.sharp, 'C'+config.sharp, 'C'+config.sharp+config.sharp, 'D'+config.sharp, 'E', 'E'+config.sharp, 'F'+config.sharp, 'F'+config.sharp+config.sharp, 'G'+config.sharp, 'G'+config.sharp+config.sharp, 'A'+config.sharp, 'B'],
			'B'+config.flat: ['C', 'D'+config.flat, 'D', 'E'+config.flat, 'E', 'F', 'G'+config.flat, 'G', 'A'+config.flat, 'A', 'B'+config.flat, 'B'],
			'B': ['C', 'C'+config.sharp, 'D', 'D'+config.sharp, 'E', 'F', 'F'+config.sharp, 'G', 'G'+config.sharp, 'A', 'A'+config.sharp, 'B']
			}

for i in a:
    if i == 'Db':
        print(a[i])
        print(len(a[i]))