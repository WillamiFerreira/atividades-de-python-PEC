niver = int(input())
soma = 0 
while niver > 0:
    soma += niver % 10
    niver //= 10
print(soma)