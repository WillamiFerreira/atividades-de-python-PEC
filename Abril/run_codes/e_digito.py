def consoante(n):
    if n in '0123456789':
     return True
    else:
        return False


def main():
    letra = (input('Digete um número e aparecerá True, ou qualquer outro caractere para aparecer false: ')).lower()
    x = print(consoante(letra))


if __name__ == '__main__':
    main()