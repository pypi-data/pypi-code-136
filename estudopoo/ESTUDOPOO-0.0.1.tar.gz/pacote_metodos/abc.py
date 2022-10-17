from abc import ABC, abstractmethod, abstractproperty

class Controle_remoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass
    
    @property
    @abstractproperty
    def marca(self):
        pass

class Controle_tv(Controle_remoto):
    def ligar(self):
        print("Ligar TV")
        print("Ligada")
    def desligar(self):
        print("Desligando TV")
        print("Desligada")
    @property
    def marca(self):
        return "LG"

class Controle_ar(Controle_remoto):
    def ligar(self):
        print("Ligar Ar")
        print("Ligada")
    def desligar(self):
        print("Desligando Ar")
        print("Desligada")
    @property
    def marca(self):
        return "philips"

controle = Controle_tv()
controle.ligar()
controle.desligar()
print(controle.marca)

controle_ar=Controle_ar()
controle_ar.ligar()
controle_ar.desligar()
print(controle_ar.marca)