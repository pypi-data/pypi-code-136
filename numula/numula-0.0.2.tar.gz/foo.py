def blah():
    return '.01'

def foo():
    x = 'blah {x} aa {x} fkjfkjf {y}'.format(x=.01, y='mf')
    ps = '.01'
    x = f'blah p{blah()} fkjf {ps}p fjfj'
    print(x)

foo()
