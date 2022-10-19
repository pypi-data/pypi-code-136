from interacao import inter


def armazenar(dados=("fulano", "00000000000", "Rua 01")):
    """
    Inserir nome, CPF e endereco como a tupla resultante da funcao inter do modulo interacao como parametro na funcao,
    ou automaticamente considerado a tupla seguinte: ("fulano", "00000000000", "Rua 01")
    """
    with open("dados_usuario.txt", "a") as file:
        file.write(f"\nNome --> {dados[0]}\nCPF --> {dados[1]}\nEndereco --> {dados[2]}\n")
        file.write("#"*20)
    print("Dados salvos!")
