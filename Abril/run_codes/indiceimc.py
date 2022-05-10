peso = float(input())
altura = float(input())
imc = peso / (altura ** 2)
print(imc)
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso normal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 35:
    print('Obeso leve')
elif 35 <=imc < 40:
    print('Obeso moderado')
elif imc >=40:
    print('Obeso mórbido')
