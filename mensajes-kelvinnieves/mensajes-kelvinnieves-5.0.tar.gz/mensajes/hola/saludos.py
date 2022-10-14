import numpy as np

def saludar():


    print('Hola,Te saludo desde saludos.saludar()')

#print(__name__)

def prueba():
    print("Esto es una  prueba de la nueva version")

def generar_array(numeros): 
    return np.arange(numeros)

class saludo:
    def __init__(self):
        print("Hola , te saludo desde Saludo __init__")

if __name__== '__main__': #el __name__ contiene el fiche una vez desde el modulo importado
    print(generar_array(5))
    #saludar()