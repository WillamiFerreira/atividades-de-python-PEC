niver = int(input('Digite sua data de nascimento somente com os 8 números: '))
soma = 0 

while niver > 0:
    soma += niver % 10 #variável responsável por isolar, somar e armazanar o último algarismo do número.
    niver //= 10 #variável que retirar o último algarismo do número depois que ele já foi adicionado a variável soma.
    
print(soma)