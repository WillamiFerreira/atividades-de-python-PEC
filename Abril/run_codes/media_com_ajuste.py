def media(p, o, i):
    if i > 8:
     return((p + o + i) / 3 + 1)
    else:
        return((p + o + i) / 3)
n1 = float(input('Primeira Nota'))
n2 = float(input('Segunda Nota'))
n3 = float(input('Terceira Nota'))

media = media(n1, n2, n3)
print(f'{round(media, 2)}')