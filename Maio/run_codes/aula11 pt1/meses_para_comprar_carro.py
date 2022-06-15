qtd_meses = 0
poupanca_incial = 10000 


preco_car_hj = int(input('Preço incial do carro: '))
while poupanca_incial < preco_car_hj: #enquanto o valor da poupança for menor que o preço do carro, o bloco será executado.
    preco_car_hj += 0.4/100 * preco_car_hj # a cada mês é somado 0.4% do valor inicial do carro daquele ano ao seu valor atual.
    poupanca_incial += 0.7/100 *  poupanca_incial # A cada mês é somado 0.7% do valor incial da poupança daquela ano ao seu valor inicial.
    qtd_meses += 1 #a cada mês que se passa e o valor da poupança não chega ao valor do carro, é somado 1 a var qtd_meses.

else: #O bloco do else é executado quanto der False em while.
    print(f'Demorará {qtd_meses} meses para comprar o carro à vista. ')

    