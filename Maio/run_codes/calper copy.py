print('CALCULADORA DE PORCENTAGEM')

valor = float(input('Digite um valor: '))
parcelas = int(input('Digite o número de parcelas: '))
perc = float(input('Digite a percentagem: %'))

parcela = valor / parcelas

juros = perc / 100 * parcela

parc_com_juros = parcela + juros

print('O valor da parcela com {}% de juros será {} reais'.format(perc,parc_com_juros))

valor_final = valor + juros * parcelas

print('O valor final da compra será {} reais'.format(valor_final))