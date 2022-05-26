qtd_meses = 0
poupanca_incial = 10000 

while True:
    preco_car_hj = int(input('Preço do carro: '))
    while poupanca_incial < preco_car_hj:
        preco_car_hj += 0.4/100 * preco_car_hj
        poupanca_incial += 0.7/100 *  poupanca_incial
        qtd_meses += 1
    else:
        print(f'É necessário {qtd_meses} meses para comprar o carro à vista. ')
        break


    