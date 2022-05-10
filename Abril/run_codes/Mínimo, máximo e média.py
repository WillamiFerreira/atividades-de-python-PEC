def media(x, x1, x2, x3, x4):
    soma = x + x1 + x2 + x3 + x4
    media = soma / 5
    return media

def maximo (z, z1, z2, z3, z4):
    nm = max(z, z1, z2, z3, z4)
    return nm

def minimo(c, c1, c2, c3, c4):
    nmi = min(c, c1, c2, c3, c4)
    return nmi

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())


maximo = maximo(n1, n2, n3, n4, n5)
print(maximo)

minimo = minimo(n1, n2, n3, n4, n5)
print(minimo)

media = media(n1, n2, n3, n4, n5)
print(media)
