def letra(n):
    if n in 'abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWXYZ' or '0123456789':
        return True
    else:
        return False

def main():
    numero_letra = input('digite algo, caso seje letra ou número a resposta será True, se não será False: ')
    print(letra(numero_letra))

if __name__ == '__main__':
    main()
