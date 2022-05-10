n1 = int(input(''))
n2 = int(input(''))
n3 = int(input(''))
n4 = int(input(''))
n5 = int(input(''))

media = (n1 + n2 + n3 + n4 + n5) / 5
print(media)
if n1 > media:
    print (n1)
elif n2 > media:
    print(n2)
elif n3 > media:
    print(n3)
elif n4 > media:
    print(n4)
elif n5 > media:
    print(n5)
else:
    print('nenhuma variável é maior que a média')