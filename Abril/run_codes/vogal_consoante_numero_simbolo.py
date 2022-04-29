def valor(n):
    if n in 'aeiouAEIOU':
        return 'Vogal'
    elif n in 'bcdfghjklmnpqrstvwxyzBCDFGHJQLMNPQRSTVWXYZ':
        return 'Consoante'
    elif n in '0123456789':
        return 'Número'
    else:
        return 'Símbolo'
def main():
    caractere = (input('Digite um caractére: '))
    print(valor(caractere))

if __name__ == '__main__':
    main()