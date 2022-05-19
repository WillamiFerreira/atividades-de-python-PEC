#O código pede números inteiros e positivos usando uma estrutura de repetição while até chegar a sua flag(valor zero), então imprime o maior e menor dos números que entraram.


def main():
    num = 1
    maior = menor = quantidade = 0
    while num != 0:
        num = int(input('Digite um número: '))
        quantidade += 1
        if quantidade == 1:
            maior = menor = num
        else:
            if num > maior:
                maior = num
            if num !=0 < menor:
                menor < num

    print(f'O menor número é {menor} e o maior é {maior}.')

if __name__ =="__main__":
    main()