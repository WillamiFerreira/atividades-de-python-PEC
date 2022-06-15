def main():
    lista = []
    pares = []
    impares =[]

    for i in range(20):#para cada número em do 0 ao 19...
        numero = int(input('Digite um número: '))#digite um número
        lista.append(numero)#o número lido é adicionado a lista indepentemente se for par ou ímpar. 
        if numero % 2 == 0:# se for par...
            pares.append(numero)#é adicionado a lista de pares
        else:
            impares.append(numero)# se nao, é adicionado a lista de impares.

    print(lista)
    print(pares)
    print(impares)

if __name__ =="__main__":
    main()

