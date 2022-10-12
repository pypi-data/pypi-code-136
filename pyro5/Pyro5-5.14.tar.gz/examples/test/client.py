from Pyro5.api import Proxy

uri = input("enter server uri: ")
t = Proxy(uri)

print(len(t))
for letter in t:
    print(letter)
# print()
# for letter in reversed(t):
#     print(letter)
# print()
# for letter in sorted(t):
#     print(letter)
# print()
# print("z" in t)
# print(t[1])
# t[1]='z'
# print(t[1])
# del t[1]
# for letter in t:
#     print(letter)
