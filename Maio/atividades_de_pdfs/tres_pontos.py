import random 
tentativas = 0 #variável que fazer o contador començar um zero
score = 0 

print('''
PORTA DA FORTUNA!
=================

Existe um super prêmio atrás de uma destas 3 portas! Advinhe qual pe a porta certa para ganhar o prêmio!

 _____  _____  _____
|     ||     ||     |
| [1] || [2] || [3] |
|    º||    º||    º|
|_____||_____||_____|
''')

while score < 3:
    tentativas += 1 #a cada rodada, essa variável adicional 1 a ela mesma.
    escolhida = int(input('\nEscolha uma porta 1, 2 ou 3: '))
    certa = random.randint(1,3)
    print('A porta escolhida foi', escolhida)
    print('A porta certa é', certa)
    
    if escolhida == certa:
        print('PARABÉNS!')
        score += 1
    else:
        print('QUE PENINHA!')

    print('Sua pontuação é', score)
print('\n** Você conseguiu! Terminou o jogo em', tentativas, 'tentativas.')
