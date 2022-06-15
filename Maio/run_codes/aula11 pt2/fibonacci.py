numero_de_termos = int(input())
primeiro, segundo = 0, 1
contador = 0

if numero_de_termos <= 0:
    print('Por favor escreva um número positivo.')
elif numero_de_termos == 1:
    print (primeiro)
else:
    while contador < numero_de_termos:
        print(f'{primeiro} ', end='')
        terceiro = primeiro + segundo
        primeiro = segundo
        segundo = terceiro
        contador += 1