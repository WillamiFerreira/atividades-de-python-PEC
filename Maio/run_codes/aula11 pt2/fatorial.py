def fatorial(n):
    if n == 0 or n == 1: #se o número for igual a zero ou um, o valor do seu fatorial é um.
        return 1
    elif n < 0: #Caso o número seja negativo, o fatorial não existe. 
        return 'Não existe fatorial de número negativo!' 
    else:
        fatorial = 1 #inicializa o valor da fatorial como 1, pois terá seu valor multiplocado depois. 
        while(n > 1):  # enquanto o número for maior que 1, o bloco é executado. 
            fatorial *= n # O farorial recebe um nomo valor, que é ele mesmo multiplicado por número menos um.
            n -= 1
        return fatorial


def main():
    numero = int(input('Digite um número: '))

    print (fatorial(numero))

if __name__ == '__main__':
    main()