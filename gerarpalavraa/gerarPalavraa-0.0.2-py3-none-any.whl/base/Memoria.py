def guardar(palavra):
    texto = []

    arq = open('base_palavras.txt', 'r')

    texto.append(arq.read())

    arq.close()

    arq = open('base_palavras.txt', 'w')

    texto.append(palavra + '\n')

    arq.writelines(texto)

    arq.close()
