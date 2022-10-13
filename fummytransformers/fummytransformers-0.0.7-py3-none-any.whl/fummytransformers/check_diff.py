a = list(open("./filenames.txt","r"))
a = [x.strip() for x in a]
b = list(open("./filenames_more.txt","r"))
b = [x.strip() for x in b]
print(len(a),len(b))
not_done = [x for x in b if x not in a]
print(not_done)
