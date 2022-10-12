def nome():
    '''
    - Solicita a entrada do nome completo a ser analizado;
    - Transforma o nome em um vetor de letras maiusculas.
    '''
    # entrada do nome completo
    print("Digite o nome completo:")
    # tranformação do nome em um vetor de letras
    nome = input().replace(" ", "").upper()

    return list(nome)


def letra_valor():
    '''
    Gera um dicionário que contém as letras maiusculas do alfabeto, com os seus 
    devidos valores (de acordo com as regras da numerologia).
    '''
    # lista das letras
    letra_list = list(map(lambda letra: chr(letra),
                      range(ord("A"), ord("Z")+1)))

    # criação do dicionário com o valor das letras
    letra_dict = {}

    for letra in letra_list:
        if letra >= 'A' and letra <= 'I':
            letra_dict[letra] = letra_list.index(letra)+1

        elif letra >= 'J' and letra <= 'R':
            letra_dict[letra] = (letra_list.index(letra)+1) - 9

        elif letra >= 'S' and letra <= 'Z':
            letra_dict[letra] = (letra_list.index(letra)+1) - 18

    return letra_dict


def vetor_numero():
    '''
    - Gera um vetor numérico com o valor das letras do nome;
    - Soma os valores do vetor;
    - Reduz o valor da soma até um digito. Com exceção dos numeros
    11, 22 e 33.
    '''
    # criação do vetor numérico relacionando ao vetor do nome
    num = list(map(lambda l: letra_valor()[l], nome()))
    num_soma = str(sum(num))

    # redução do valor
    num_redu = 0
    for n in num_soma:
        num_redu += int(n)

        if num_redu > 9:
            if num_redu == 11 or num_redu == 22 or num_redu == 33:
                break
            else:
                num_redu = num_redu % 10 + num_redu // 10

    return num_redu


def significa_num(num_redu):
    '''
    Apresenta o significado do número que foi gerado pela soma das letras do nome.

    num_redu = processamento.vetor_numero()
    '''
    if num_redu == 1:
        print(f"Seu número é {num_redu}: ")
        print("É uma pessoa com senso de liderança e independência. Trata-se de um indivíduo muito determinado e que não espera por ninguém para conseguir o que quer. Porém, precisa tomar cuidado com egocentrismo e arrogância.")

    elif num_redu == 2:
        print(f"Seu número é {num_redu}: ")
        print("Para esta pessoa, a vontade do outro é mais importante que a sua própria vontade. No entanto, não se engane! Um indivíduo com este nome não se deixa levar facilmente pelas emoções.")

    elif num_redu == 3:
        print(f"Seu número é {num_redu}: ")
        print("Trata-se de um indivíduo divertido, alegre e otimista. Uma pessoa com este número gosta de agir e não desiste com facilidade. Entretanto, é alguém que gosta também de falar e não conhece os próprios medos.")

    elif num_redu == 4:
        print(f"Seu número é {num_redu}: ")
        print("Uma pessoa com este número é organizada e prática. Este indivíduo gosta de estabilidade e, por isso, quase sempre é racional. Ele está sempre em busca de afeto, embora seja considerado um pouco frio emocionalmente falando.")

    elif num_redu == 5:
        print(f"Seu número é {num_redu}: ")
        print("Trata-se de uma pessoa curiosa. Por isso, adora viajar e experimentar coisas novas. Por outro lado, por ser mais independente, não gosta de receber ordens. Além disso, é divertida, envolvente e considera acontecimentos imprevisíveis como um bom estímulo.")

    elif num_redu == 6:
        print(f"Seu número é {num_redu}: ")
        print("Trata-se de um indivíduo muito familiar e que, portanto, gosta de afeto. Uma pessoa com este número é emotiva, protetora e, por querer um lar feliz, está sempre à procura do equilíbrio entre razão e emoção.")

    elif num_redu == 7:
        print(f"Seu número é {num_redu}: ")
        print("Uma pessoa com este número adora de ficar sozinha, tranquila e em paz na sua privacidade. Por este motivo, é considerada racional, individualista, com alguns poucos amigos. No entanto, não se engane! Em seu interior, há sentimentos profundos.")

    elif num_redu == 8:
        print(f"Seu número é {num_redu}: ")
        print("Um indivíduo com este número está sempre à procura de justiça e respeito. Também é ambicioso e gosta de poder. Ainda, esta pessoa está sempre em busca de ser equilibrada e eficiente.")

    elif num_redu == 9:
        print(f"Seu número é {num_redu}: ")
        print("Uma pessoa com este número é generosa e humanitária. Por esta razão, geralmente, possui postura de irmão mais velho. Este indivíduo também atrai o amor de todos e pratica a bondade.")

    elif num_redu == 11:
        print(f"Seu número é {num_redu}: ")
        print("Um indivíduo com este número deseja viver em um mundo melhor. Em geral, é criativo, corajoso e imaginativo. Ele quer sempre ser considerado uma inspiração para os outros.")

    elif num_redu == 22:
        print(f"Seu número é {num_redu}: ")
        print("Esta pessoa é paciente, otimista e quer sempre ajudar. O indivíduo com este número faz de tudo para beneficiar a si mesmo e, também, aos outros.")

    elif num_redu == 33:
        print(f"Seu número é {num_redu}: ")
        print("Uma pessoa com este número vê a necessidade dos outros como o que há de mais importante e, portanto, gosta de praticar o amor sempre. Ela gosta de ver beleza em qualquer coisa e tem ótimas ideias e esperanças sobre a vida sentimental e familiar.")


if __name__ == "__main__":
    significa_num(vetor_numero())
