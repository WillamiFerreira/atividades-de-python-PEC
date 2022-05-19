import random

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
score = 0
for rodada in range(3):
    portaescolhida = int(input('\nEscolha uma porta (1, 2 ou 3): '))
    portacerta = random.randint(1, 3)
    print('A porta escolhida foi {}'.format(portaescolhida))
    print('A porta certa é {}'.format(portacerta))
    if portaescolhida == portacerta:
        print("Parabéns!")
        score += 1
    elif portaescolhida != portacerta:
        print('Que peninha!')
    else:
        print('Valor inválido')


print('A sua pontuação foi de {}'.format(score))