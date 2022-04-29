def letra(n):
    if n in 'ABCDEFGHIJKLMNOPQSRTUVWXYZ':
        return True
    else:
        return False
def main():
    caractere = input('Digite alguma coisa: ').upper()

    print(letra(caractere))

        
if __name__=='__main__':
    main()