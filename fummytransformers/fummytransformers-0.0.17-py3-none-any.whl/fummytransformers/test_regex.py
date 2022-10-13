from fummytransformers import files


import re
s = "Example String\na test"

replaced = re.sub('a', 'aa', s)
print(replaced)

xx = "guru99,education is fun"
r1 = re.search(r"[\d]+", xx)
print(r1.group(0))
