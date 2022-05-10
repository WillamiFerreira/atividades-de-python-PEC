#def alo_nome(nome = 'Paulo'):
#    print('Alô' + nome + '!')

#meu_nome = 'Maria'
#alo_nome(meu_nome)

#def diga_nome(nome, idade):
#    print(f'olá, {nome}, você tem {idade} anos de idade')
    
#diga_nome('João', 21)

#def dobro(x):
#    return x * 2

#a = int(input('Digite um valor inteiro: '))
#b = dobro(a)
#print(f'{b}')

def dobro_e_triplo(n):
    dobro = n * 2
    triplo = n * 3
    return dobro, triplo


var = int(input('Dogite um número: '))
x2, x3 = dobro_e_triplo(var)
print(f'{var}{x2}')
print(f'{var}{x3}')
