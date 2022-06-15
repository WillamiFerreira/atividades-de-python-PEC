#módulo que recebe o tamanho da lista e imprime uma com todos os valores igual a 0.
def lista0(n):
    lista0 = []
    for i in range(n):
        lista0.append(0)
    print(lista0)

#módulo que recebe o tamanho da lista e imprime uma com os valores começando de 1 até n.
def lista1(n):
    lista1 = []
    for i in range(n):
        lista1.append(i + 1)
    print(lista1)

#módulo que ler n números no teclado e imprime uma lista com o números na ordem que foi lida. 
def lista2(n):
    lista2 = []
    for i in range(n):
        lista2.append(int(input(f'Digite o {i + 1}º número da lista: ')))
    print(lista2)

#módulo que ler n números no teclado e imprime uma lista com o números na ordem inversa a que foi lida.
def lista3(n):
    lista3 = []
    for i in range(n):
        lista3.append(int(input(f'Digite o {i + 1}º número da lista: ')))
    lista3.reverse() #usando o método reverse para inverter a ordem dos elementos depois que todos os números foram armazenados na lista3.
    print(lista3)

def main():
    quantidade = int(input('Digite o tamanho da lista: '))
    lista0(quantidade)
    lista1(quantidade)
    lista2(quantidade)
    lista3(quantidade)


if __name__ == '__main__':
    main()