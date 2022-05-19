deposito_incial = float(input('Qual o valor do depósito incical? '))
taxa_juros = float(input('Qual o valor da taxa de juros anual? '))
valor_acumulado = deposito_incial
anos = 0
while valor_acumulado  < 2*deposito_incial:
    valor_acumulado += taxa_juros
    x = valor_acumulado
    print(f'{x:.2f}')
    anos += 1

print('levará {} anos para o valor acumulado valer o dobro do depósito incial'.format(anos))
