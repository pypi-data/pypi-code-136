import base.Memoria
import gerador.Palavra

arq = open('base_palavras.txt', 'w')
arq.writelines('')
arq.close()

resp = int(input("Quantas palavras deseja gerar? "))

for i in range(0, resp):
    base.Memoria.guardar(f"{i+1}: " + gerador.Palavra.gerarLetra())

resp = input("Deseja visualizar as palavras geradas no arquivo base_palavras? ")

if resp[0].lower() == 's':
    arq = open('base_palavras.txt', 'r')
    print(arq.read())
    arq.close()
