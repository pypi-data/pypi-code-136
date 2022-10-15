import fileinput

n = 0
for line in fileinput.input():
    n += 1
print(n)
