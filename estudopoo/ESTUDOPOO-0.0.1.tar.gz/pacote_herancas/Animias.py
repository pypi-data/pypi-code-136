class Animal:
    def __init__(self, numero_patas):
        self.numero_patas = numero_patas

    def __str__ (self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)
    
class Cachorro(Mamifero):
    def __init__(self, latir=False, **kw):
        self.latir = latir
        if (latir==True):
            print("Au Au Au")
        super().__init__(**kw)


class Gato(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelo, numero_patas):
        super().__init__(cor_bico=cor_bico, cor_pelo=cor_pelo, numero_patas=numero_patas)

gato=Gato(numero_patas=4, cor_pelo="preto")
print(gato)

ornitorrinco = Ornitorrinco(numero_patas=3, cor_pelo="marrom", cor_bico="laranja")
print(ornitorrinco)

cachorro=Cachorro(numero_patas=4, cor_pelo="branco", latir=True)
print(cachorro)