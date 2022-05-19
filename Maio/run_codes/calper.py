print('CALCULADORA DE PORCENTAGEM')

valor = float(input('Digite um valor: '))
parcelas = int(input('Digite o número de parcelas: '))
perc = float(input('Digite a percentagem: %'))


parcela = valor / parcelas
juros = perc / 100 * parcela
parcela_com_juros = parcela + juros

print('o valor da parcela com juros é de {}'.format(parcela_com_juros))

valor_total = valor + juros * parcelas

print(valor_total)