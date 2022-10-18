import random as r


c = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
v = ['a', 'e', 'i', 'o', 'u']


def create_name(size):
    """
    Returns a randomly created name with 'size' syllables
    """
    nome = ''
    vez = r.randint(0, 1)
    if vez:
        for n in range(size):
            nome += r.choice(c)
            nome += r.choice(v)
    else:
        for n in range(size):
            nome += r.choice(v)
            nome += r.choice(c)
    return nome.capitalize()


def create_name_and_lastname(size_name, size_lastname):
    """
        Returns a randomly created name and last name with 'size_name' and 'size_lastname' syllables
    """
    l = ['de', 'da', 'of', 'thee', 'from', 'do']

    vez = r.randint(0, 1)
    return f"{create_name(size_name)} {create_name(size_lastname)}" if vez \
        else f"{create_name(size_name)} {r.choice(l)} {create_name(size_lastname)}"


