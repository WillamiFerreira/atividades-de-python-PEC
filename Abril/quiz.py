def analise(n):
    x = n
    if x in ('VARIAVEL', 'VARIÁVEL'):
        return ' você acertou, parabéns :)'
    else:
        return('Você errou :(')
    
def main():
    print('Vamos jogar')
    print('No pyhton, como se chama uma caixa usada para armazanar dados? ')
    
    resposta = input().upper()
    print(analise(resposta))

if __name__ == '__main__':
    main()