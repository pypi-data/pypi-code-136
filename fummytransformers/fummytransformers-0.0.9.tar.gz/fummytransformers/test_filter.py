import glob
# from frenchnlp import files

txts = glob.glob("*.txt")

total = []
for t in txts:
    total += list(open(t, "r"))
    total = [x.strip() for x in total if x.strip() != "2"]

print(list(set(total)))


# print(len(set(total)))
