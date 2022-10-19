def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
        lista_produtos = []
        for linha in a:
            dado = linha.split(',')
            dado[2] = dado[2].replace('\n', '')
            dado[1] = float(dado[1])
            dado[2] = float(dado[2])
            lista_produtos.append(dado)
    except:
        print('Erro ao ler arquivo!')
    else:
        return lista_produtos    
    finally:
        a.close
