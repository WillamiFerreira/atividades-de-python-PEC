idade = 1 #variável que define o valor da idade como 1. Ela é importânte para incializar o bloco do while.
nu_pessoas = 0 #define o número de pessoas inincialmente em 0.
soma_das_idades = 0 #define como zero o resulado da soma dos idades das pessoas.
menor = maior = 0 #define como zero a idade da pessoa mais nova e a mais velha.
print('Digite zero para parar')
while idade > 0:
    idade = int(input(f"Idade da {nu_pessoas + 1}º pessoa: "))
    nu_pessoas += 1 #contador no número de pessoas que soma 1 ao seu valor a cada volta do laço.
    soma_das_idades += idade #variável que calcula e armazena em si a soma das idades das pessoas que são, a cada volta, adicionadas.
    #da linha 11 a 17 está o algoritimo que descobre qual é a menor e maior idade.
    if nu_pessoas == 1:
        maior = menor = idade
    else:
        if idade > maior:
            maior = idade
        if idade !=0 < menor:
            menor = idade


numero_de_pessoas = nu_pessoas - 1 #variável que subtrai uma pessoa da soma total de pessoas, pois o zero não deve ser considerado.
media = soma_das_idades / nu_pessoas - 1 #variável que retira um uma pessoa do total de pessoas, para fazer o corretamente o calculo da média de todas as idades.

#formatação das saídas
print(f'=-' *10)
print(f"Foi lido {numero_de_pessoas} pessoas." )
print(f'A média entre as idades das pessoas é {media:.2f} anos.')
print(f"A pessoa mais velha tem {maior} anos e a pessoa mais nova tem {menor} anos.")
print(f'=-' *10)
