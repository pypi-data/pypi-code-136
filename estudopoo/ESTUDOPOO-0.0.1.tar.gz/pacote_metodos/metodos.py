class Pessoa:
    
    def __init__(self, nome=None, idade=None):
        self.nome=nome
        self.idade=idade
    
    @classmethod
    def criar_data_nascimento(cls, ano, mes, dia, nome):
        idade=2022-ano
        return cls(nome, idade)

    @staticmethod
    def e_maior_de_idade(idade):
        return idade>=18

p = Pessoa.criar_data_nascimento(1982, 10, 16, "Felipe")
print(p.nome, p.idade)

print(Pessoa.e_maior_de_idade(10))
print(Pessoa.e_maior_de_idade(25))

