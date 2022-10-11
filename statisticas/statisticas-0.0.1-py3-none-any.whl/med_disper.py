from statistics import mean
import math

def var_amostral(*,valores:list, media:float):
    qtd = len(valores)
    soma = sum([(valor - media)**2 for valor in valores])
    return soma/(qtd-1)

def amplitude(valores:list):
    valores.sort()
    menValor = valores[0]
    maxValor = valores[len(valores)-1]
    return maxValor - menValor

def desvio_padrao(valores:list):
    return math.sqrt(var_amostral(valores=valores, media=mean(valores)))

def coeficinete_variacao(valores:list):
    return (desvio_padrao(valores)/mean(valores))*100