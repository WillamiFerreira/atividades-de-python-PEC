#módulo que ler n números, os aniciona um uma lista e imprime a ordem inversa.
def reais_inversos(n):
    lista1 = []
    for i in range(n):
        lista1.append(float(input()))
    lista1.reverse()
    print(lista1)

#módulo que ler n notas e impreme um lista com elas e a média.
def notas(n):
    lista_de_notas = []
    if n == 0:
        print('SEM NOTAS')
    for i in range(n):
        lista_de_notas.append(float(input(f'Digite a sua {i + 1}º nota: ')))
    print(lista_de_notas)
    print(f'{sum(lista_de_notas) / n:.1f}')

#Módulo que ler n letras e inprime a quantidade de vogais lidas e a lista das consoantes lidas.
def vogais_consoantes(n):
    vogais = []
    consoantes = []
    for i in range(n):
        letra = str(input('Digite uma letra: '))
        if letra in 'AaEeIiOoUu':
            vogais.append(letra)
        else:
            consoantes.append(letra)

    print(len(vogais))
    print(consoantes)

def main():
    
    tamanho = int(input('Digite o tamanho da lista: '))
    reais_inversos (tamanho)
    notas (tamanho)
    vogais_consoantes (tamanho)

if __name__ == "__main__":
    main()