opcoes = True
while opcoes == True:
    opcoes = int(input('''
OPÇÕES:
1 - SAUDAÇÃO
2 - BRONCA
3 - FELICITAÇÃO
0 - FIM
Digite sua escolha: '''))
    
if opcoes == 1:
    print('Olá, como vai?')
    opcoes = False
elif opcoes == 2:
    print('Vamos estudar mais.')
    opcoes = False

elif opcoes == 3:
    print('Meus Parabéns!')
    opcoes = False

elif opcoes == 0:
    print('Fim de serviço')
    opcoes = False
    
else:
    print('Opção inválida')
    opcoes = False
