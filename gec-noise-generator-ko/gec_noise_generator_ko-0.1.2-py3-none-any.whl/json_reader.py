from __future__ import absolute_import
import json
import os
current_file = os.path.dirname(__file__)
f = open(current_file + '/resources/EXSC2102112091.json')
data = json.load(f)
with open(current_file + "/resources/test" + "_noised.txt", 'w', encoding="UTF-8") as noised:
    texts = data['document']
    for text in texts:
        for a in text['paragraph']:
            if a['corrected_form'] != '.' or a['corrected_form'][0] != "#":
                noised.write(a['corrected_form'] + "\n")
noised.close()
f.close()
