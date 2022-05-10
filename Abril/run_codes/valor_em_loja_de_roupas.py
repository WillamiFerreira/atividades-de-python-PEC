def desconto(valor):
    v = valor * 0.09
    return v

def parcela(valor):
    p = valor / 5
    return p

def juros_1(valor):
    j1 = valor / 10
    return j1

def juros(valor):
    j = valor * 0.17 / 10
    return j

valor = float(input())
x1 = valor - desconto(valor) 
x2 = parcela(valor)
x3 = juros(valor)
x4 = juros_1(valor)
juros1 = x4 + x3
print(f'{x1:.2f}')
print(f'{x2:.2f}')
print(f'{juros1:.2f}')
