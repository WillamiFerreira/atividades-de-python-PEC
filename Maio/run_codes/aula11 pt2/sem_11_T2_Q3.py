flag = int(input('Digite o valor de n: '))
divisor = 1
h = 0
while divisor < flag:
    if divisor == 1:
        h = 1
        divisor += 1
    else:
        h += (1/divisor)
        divisor += 1

print(f'{h:.4f}')