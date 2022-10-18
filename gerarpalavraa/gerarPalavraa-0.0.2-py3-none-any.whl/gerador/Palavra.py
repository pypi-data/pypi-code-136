import random

def gerarLetra():
    vogal = 'aeiou'
    consoante = 'bcdfghjklmnpqrstvwxyz'
    dissilaba = ''

    for i in range(0,2):
        dissilaba += random.choice(consoante) + random.choice(vogal)

    return dissilaba