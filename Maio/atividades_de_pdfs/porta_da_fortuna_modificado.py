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
jogando = True
score  = 0
while jogando == True:
    portaescolhida = int(input('Escolha uma porta: '))
    portacerta = random.randint(1,3)
    print('\nA porta escolhida foi', portaescolhida)
    print('\nA porta certa é', portacerta)

    if portaescolhida == portacerta:
        print('\nPARABÉNS! :)')
        score += 1
    else:
        print('\nQUE PENINHA :(')
        score = 0

    print('\nSua pontuação é', score)
    play_again = str(input('\nDeseja jogar novamente? (s/n)')).strip()[0].lower()#FORMATANDO A SAÍDA PARA REDURZIR AS CHANCES DE ERRO POR DIGITAÇÃO DO USUÁRIO.
    if play_again == 'n':
        jogando = False

print('\nSua pontuação final é de', score)
print("OBRIGRADO POR JOGAR!")