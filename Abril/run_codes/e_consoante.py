def consoante(n):
    if n in 'bcdfghjklmnpqrstvwxyz':
     return "True"
    else:
        return 'False'


def main():
    letra = (input('Digite alguma coisa, se for consoante, o retorno será True, se não será False ')).lower()
    x = print(consoante(letra))
      
        
if __name__ == '__main__':
    main()