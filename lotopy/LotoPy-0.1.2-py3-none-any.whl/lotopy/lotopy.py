import random

def megasena( qtd_apostas:int, qtd=6):
    FAIXA = 60
    QTD_MIN = 6
    QTD_MAX = 15
    NUMEROS = range(1, FAIXA + 1)
    lista = []

    if qtd != '':
        if qtd < QTD_MIN or qtd > QTD_MAX:
            print('quantide de numeros para megasena deve estar entre: {} e {}'.format(QTD_MIN,QTD_MAX))
        else:
            for i in range(0, qtd_apostas):
                x = random.sample(NUMEROS, qtd)
                lista.append(x)
            return lista
    else:
        for i in range(0, qtd_apostas):
            x = random.sample(NUMEROS, QTD_MIN)
            lista.append(x)
        return lista

def lotofacil(qtd_apostas:int, qtd=15):
    FAIXA = 25
    QTD_MIN = 15
    QTD_MAX = 18
    NUMEROS = range(1,FAIXA + 1)
    lista = []

    if qtd != '':
        if qtd < QTD_MIN or qtd > QTD_MAX:
            print('quantide de numeros para lotofacil deve estar entre: {} e {}'.format(QTD_MIN,QTD_MAX))
        else:
            for i in range(0, qtd_apostas):
                x = random.sample(NUMEROS, qtd)
                lista.append(x)
            return lista
    else:
        for i in range(0, qtd_apostas):
            x = random.sample(NUMEROS, QTD_MIN)
            lista.append(x)
        return lista

def quina( qtd_apostas:int, qtd=5):
    FAIXA = 80
    QTD_MIN = 5
    QTD_MAX = 15
    NUMEROS = range(1, FAIXA + 1)
    lista = []

    if qtd != '':
        if qtd < QTD_MIN or qtd > QTD_MAX:
            print('quantide de numeros para quina deve estar entre: {} e {}'.format(QTD_MIN,QTD_MAX))
        else:
            for i in range(0, qtd_apostas):
                x = random.sample(NUMEROS, qtd)
                lista.append(x)
            return lista
    else:
        for i in range(0, qtd_apostas):
            x = random.sample(NUMEROS, QTD_MIN)
            lista.append(x)
        return lista

if __name__=='__main__':
    print('Numeros da Megasena:')
    numeros = megasena(8)
    for i in numeros:
        print(i)

    print('Numeros da lotofacil:')
    numeros = lotofacil(5)
    for i in numeros:
        print(i)

    print('Numeros da quina:')
    numeros = quina(5,15)
    for i in numeros:
        print(i)
