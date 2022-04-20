def msg(m):
    if m == 'v':
        return ('SIGA')
    elif m == 'a':
        return ('ATENÇÃO')
    elif m == 'e':
         return ('PARE')
    else:
        return('Voce Não digitou V, A ou E')

def main():
 cor = input()
 print(msg(cor))

 if __name__ == '__main__':
    main()