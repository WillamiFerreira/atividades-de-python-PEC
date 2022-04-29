cor  = input('“V” é verde; “A” é amarelo; “E” é vermelho: ').upper()
if cor == 'V':
    print('Siga')
elif cor == 'A':
    print('Atenção')
elif cor == 'E':
    print('Pare')
else:
    print('Você não digitou nenhuma das três opções.')