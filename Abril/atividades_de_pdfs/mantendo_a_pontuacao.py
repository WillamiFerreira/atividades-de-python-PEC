def score_final(n):
    if n == 4:
        return ('muito bem!')
    else:
        return('tente novamente')

def main():
    score = 0
    print('Vamos jogar')

    print('''1) No pyhton, como se chama uma caixa usada para armazanar dados?
    a) Texto
    b) variável
    c) uma caixa de sapatos
    ''')

    resposta = input().lower()

    if resposta == 'b':
        score = score + 1
        print ('Você acertou')
    elif resposta == 'c':
        print ('Você errou')
    elif resposta == 'a':
        print ('Você errou')
    else:
        print ('Você não marcou nenhuma das alternativas')
         

    print ('''2. Quais o menor e o maior país do mundo?
    a) Vaticano e Rússia
    b) Nauru e China
    c) Mônaco e Canadá''')
    resposta = input().lower()
    if resposta == 'a':
        score = score + 1
        print ('parabéns ;)')
    elif resposta == 'b':
        print ('Você errou')
    elif resposta == 'c':
        print ('Você errou')
    else:
        print ('Você não marcou nenhuma das alternativas')

    print('''3. Qual o nome do presidente do Brasil que ficou conhecido como Jango?
    a) Getúlio Vargas
    b) João Figueiredo
    c) João Goulart''')
    resposta = input().lower()
    if resposta == 'a':
        print ('você errou :(')
    elif resposta == 'b':
        print ('Você errou :(')
    elif resposta == 'c':
        score = score + 1
        print ('Você acertou!!! Parabêns!!! :)')
    else:
        print('você não marcou nenhuma das alternativas')

    print('''18. Qual a nacionalidade de Che Guevara?
    a) Panamenha
    b) Boliviana
    c) Argentina
    ''')
    resposta = input().lower()
    if resposta == 'a':
        print('Você errou :(')
    elif resposta == 'b':
        print('Você errou :(')
    elif resposta == 'c':
        score = score + 1
        print('Parabêns, você acertou!!! :)')

        print('Sua pontuação final é', score)

        x = score
        print(score_final(x))

if __name__ == '__main__':
    main()