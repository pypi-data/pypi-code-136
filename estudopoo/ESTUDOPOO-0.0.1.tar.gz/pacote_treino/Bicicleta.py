class bicicleta:
    
    def __init__(self, cor, ano, valor):
        self.cor = cor
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print("Plim PLim ...")
    
    def freiar(self):
        print("Biciclta parada")
    
    def correr(self):
        print("Saindo do lugar")

    def get_cor(self):
        return self.cor
    def __str__ (self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

b1 = bicicleta("vermelha", 1988, 30.00)
b2 = bicicleta("azul", 1990, 55.00)
b1.buzinar()
b1.correr()
b1.freiar()
print(b1.ano, b1.cor)
print(b1.get_cor())
print(b2)



