def consultar():
    with open("dados_usuario.txt", "r") as file:
        arq = file.read()
        print(arq)