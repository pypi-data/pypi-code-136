class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("ligando motor")

    def __str__ (self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"


class Motocicleta (Veiculo):
    pass

class Carro (Veiculo):
    pass

class Caminhao (Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

moto = Motocicleta("preta", "ert-1235", 2)

carro = Carro("vermelho", "rtp-3059", 4)

caminhao = Caminhao("branco", "iuj-0876", 8, True)

caminhao.esta_carregado()

print(caminhao)
print(moto)
print(carro)