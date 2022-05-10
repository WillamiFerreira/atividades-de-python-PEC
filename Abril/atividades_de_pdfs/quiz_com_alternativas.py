def analise(n):
    if n == 'A':
        return('Não - texto é um tipo de dado :(')
    elif n == 'B':
        return('Correto!! :)')
    elif n == 'C':
        return('Não seja bobo :(')
    else:
        return('Você não escolheu nenhuma das opções.')

def main():
    print('Vamos jogar')
    print('No pyhton, como se chama uma caixa usada para armazanar dados? ')
    print('''
    a - Texto
    b - variável
    c - uma caixa de sapatos
    ''')
    
    resposta = input().upper()
    print(analise(resposta))

if __name__ == '__main__':
    main()