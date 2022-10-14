def calcular():
    operacao = input(f"""
Digite o tipo de operação matemática desejada: \n
\033[1;49;30m[ + ] Adição\033[m
\033[1;49;31m[ - ] Subtração\033[m
\033[1;49;32m[ * ] Multiplicação\033[m
\033[1;49;33m[ / ] Divisão\033[m
\033[1;49;34m[ **] Potencialização\033[m
\033[1;49;35m[ % ] Módulo\033[m
""")

    primeiro_numero = int(input(f"\033[1;49;36mDigite um número: \033[m\n"))
    segundo_numero = int(input(f"\033[1;49;36mDigite outro número: \033[m\n"))

    if operacao == "+":
        resultado = primeiro_numero + segundo_numero
    
    elif operacao == "-":
        resultado =primeiro_numero - segundo_numero
      
    elif operacao == "*":
        resultado = primeiro_numero * segundo_numero
  
    elif operacao == "/":
        resultado = primeiro_numero / segundo_numero
        
    elif operacao == "**":
        resultado = primeiro_numero ** segundo_numero
        
    elif operacao == "%":
        resultado = primeiro_numero % segundo_numero

    else:
        print("Operador inválido!!!")
        
    print(f"O resultado da operação \033[1;49;36m{primeiro_numero}\033[m \033[1;49;36m{operacao}\033[m \033[1;49;36m{segundo_numero}\033[m é \033[1;49;36m{resultado:.2f}\033[m ")

    continuar_calculo() # Adiciona a função para continuar a calcular ou não.

def continuar_calculo():
    novo_calculo = input("Quer fazer outro cálculo? \nDigite 'S' ou 'N': \n.")

    if novo_calculo.upper() == "S":
        calcular()
    elif novo_calculo.upper() == "N":
        print("Bons estudos!!!")
    else:
        print("Opção inválida!!!")
        continuar_calculo()
        
calcular()