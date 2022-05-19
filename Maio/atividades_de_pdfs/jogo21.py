import random
pontuacao = 0
jogando = True
while jogando == True:
    jogar = input('Aperte enter para jogar um número: ')
    x = random.randint(1, 10)
    pontuacao += x
    again = input('Deseja continuar? (s/n)').strip()[0].lower()
    if again == 'n':
        jogando = False

print('\nSua pontuação foi de', pontuacao, 'pontos.')
if pontuacao == 21:
    print('PARABÉNS!!')
elif pontuacao > 21:
    print('Você passou de 21 pontos')
else:
    print('Você não conseguiu 21 pontos')
print('FIM DE JOGO')