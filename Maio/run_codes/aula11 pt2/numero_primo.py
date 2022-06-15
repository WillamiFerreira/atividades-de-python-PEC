numero = int(input('Digite um número: '))
eprimo = 0

for i in range(1,( numero + 1)):
    if numero % i == 0:
        eprimo += 1
    
if eprimo == 2:
    print(True)
else:
    print(False)