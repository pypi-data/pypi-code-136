import re
from fummytransformers import *

fns = ['1410000', '300000', '140000', '330000', '40000', '480000', '10000', '20000', '290000', '70000',
       '50000', '320000', '100000', '240000', '110000', '250000', '310000', '30000', '370000', '260000']


all_files = iter_documents(".", "pickle")
# print(list(all))
# print(len(list(all_files)))
# print(all_files)
to_del = []
# for xn in fns:
for y in all_files:
    # print(re.search(r"\d+", y).string)
    if re.search(r"\d+", y).group(0) in fns:
        to_del.append(y)
# print(to_del)
# print(len(to_del))
# print(to_del[0])
for f in to_del:
    os.remove(f)
# for r, d, files in os.walk("."):
#     print([file for file in filter(lambda file: file.endswith("."+"pickle"), files)])
