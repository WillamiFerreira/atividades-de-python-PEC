
import re


def conversor(code):
    if code == 'H':
        return 5.50
    elif code == 'C':
        return 5.80
    elif code == 'M':
        return 4.50
    elif code == 'A':
        return 7.00
    elif code == 'Q':
        return 4.00
    elif code == 'X':
        return 0
    

def main():
    total = 0
    code = ''
    print('''
 -=-=-=-=-=-CARDÁPIO=-=-=-=-=-=

  CÓDIGO      PRODUTO     PREÇO
    H        Hamburger    5.50 
    C      Cheeseburger   6.80
    M       Misto Quente  4.50
    A        Americano    7.00
    Q      Queijo Prato   4.00
    X    PARA TOTAL DA CONTA
    ''')
    while code != 'X':
        code = str(input('Digite o código das suas compras: ')).upper().strip() [0]
        x = conversor(code)
        total += x
    print('Total a pagar é {:.2f} reais'.format(total))

if __name__ == "__main__":
    main()