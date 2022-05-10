val = float(input())
des = float(input())
aumento = des/100 * val + val
desconto = val - val * des/100
print(f'{aumento:.2f}')
print(f'{desconto:.2f}')
