listaa = []
listab = []
listac = []

#Parte que ler e adiciona os 25 números da primeira lista.
for i in range(25):
    listaa.append(int(input('Digite o ')))

#Parte que ler e adiciona os 25 números da segunda lista.
for i in range(25):
    listab.append(int(input()))

#Parte que adiciona o elemento de índice i da listaa e depois da listab a listac.
for i in range(25):
    listac.append(listaa[i])
    listac.append(listab[i])
    
print(listaa)
print(listab)
print(listac)