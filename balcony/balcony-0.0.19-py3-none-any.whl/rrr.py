def kayan_yazi(_list, window=5):
    length = len(_list)
    until = length - window
    for i in range(until+1):
        yield _list[i:i+window]
        
for x in kayan_yazi(list(range(100))):
    print(x)
    print('---'*20)