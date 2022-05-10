valor_da_compra = float(input('Digite o valor da sua compra: R$'))
prestacao = 0
x =  0
print('Você pode pagar em: ')
for _ in range(1, 25):
    x += prestacao + 1
    print(f'{x}x de R$ {valor_da_compra / x :.2f}')