'''
funcion que pasamos un número por parametro y nos devuelve todos 
los numero primos 2...N
'''
def numPrimos(n):
    print("-----------------------------")
    print("Numeros primos hasta el",n,":")
    print("-----------------------------")
    for aux in range(2,n+1):
        if not((aux % 2 == 0 and aux != 2) or (aux % 3 == 0 and aux != 3 ) or (aux % 5 == 0 and aux!=5) or (aux % 7 == 0 and aux != 7)):
            if aux != 2:
                print(', ', end='')
            print(aux, end='')
    print('.')
    
numPrimos(int(input("Introduce un número : ")))