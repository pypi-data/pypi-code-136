def entrada_dados():
    
    ano_nascimento = int(input("Digite o ano do seu nascimento:\n"))
    ano_atual = int(input("Digite o ano atual:\n"))
    calculo_idade(ano_nascimento, ano_atual)
    
def calculo_idade(ano_nascimento, ano_atual):
    calculo_idade = ano_atual - ano_nascimento
    print(f"Sua idade e de {calculo_idade} anos!")

    if calculo_idade >= 18:
        print("Você ja tem maior idade")
    else:
        print("Você ainda não atingiu maior idade")
