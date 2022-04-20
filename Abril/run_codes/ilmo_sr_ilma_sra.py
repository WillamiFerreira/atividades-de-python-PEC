def sex(n):
    if n == '1':
        return 'Ilmo Sr.'
    else:
        return 'Ilma Sra.'

def main():
    nome = input()
    sexo = input()
    print( sex(sexo) , nome)
if __name__ == '__main__':
    main()