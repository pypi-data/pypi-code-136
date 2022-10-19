from .transformartxt import arquivoexiste, lerarquivo

def precoporlitro(nome):
    """Função que por padrão retorna uma lista contendo a marca do produto e o calculo do preço por litro.

    Args:
        nome: recebe um arquivo no formato .txt contendo a marca do produto, a quantidade em litros e o preço
        separados por vírgula e com cada produto a ser testado em uma linha.
        Exemplo: 'coca-cola,0.350,2.99
                  pepsi,2,6.00
                  Guaraná,1,4.99'

    Returns:
        list: retorna uma lista contendo listas com as marcas dos produtos e os preços por litro.
        Exemplo: [coca-cola,8.54][pepsi,3][Guaraná,4.99]
    """
    try:
        arquivoexiste(nome)
    except:
        print('Erro. Arquivo não encontrado!')
    else:
        try:
            lista = lerarquivo(nome)
            for nalista in lista:
                ppl = f'{nalista[2] / nalista[1]:.2f}'
                nalista.append(float(ppl))
                del nalista[2]
                del nalista[1]
        except:
            print('Erro ao calcular preço por litro!')
        else:
            return lista


def melhorpreco(nome):
    """Função que por padrão um arquivo de texto no formato .txt e retorna uma lista contendo a marca do produto e o calculo do preço por litro.

    Args:
        nome: recebe um arquivo no formato .txt contendo a marca do produto, a quantidade em litros e o preço
        separados por vírgula e com cada produto a ser testado em uma linha.
        Exemplo: 'coca-cola,0.350,2.99
                  pepsi,2,6.00
                  Guaraná,1,4.99'

    Returns:
        list: retorna uma lista contendo a marca do produto e o preço por litro do produto com melhor preço por litro.
    """
    lista_produtos = precoporlitro(nome)
    melhor_preco = []
    for contagem, valores in enumerate(lista_produtos):
        if contagem == 0:
            melhor_preco.append(valores[0])
            melhor_preco.append(valores[1])
        else:
            if melhor_preco[1] > valores[1]:
                melhor_preco.clear()
                melhor_preco.append(valores[0])
                melhor_preco.append(valores[1])
    return melhor_preco