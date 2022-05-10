
par = 0
impar = 0

for _ in range(100):
        numero = int(input('Digite um número inteiro positivo:  '))
        if numero % 2 == 0:
                par += 1
        if numero % 2 == 1:
                impar += 1
print(par)
print(impar)