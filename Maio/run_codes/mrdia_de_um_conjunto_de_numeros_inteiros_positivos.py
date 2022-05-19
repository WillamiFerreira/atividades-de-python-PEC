
cont = 0
soma = 0
while True:
    numero = int(input('Digite um número positivo inteiro: '))
    cont += 1
    soma +=  numero
    if numero == 0: break

media = soma / (cont - 1)

print(f'{media:.2f}')

