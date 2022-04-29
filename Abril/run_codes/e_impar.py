def impar(x):
    if x % 2 == 1:
      print ('True')
    else:
     print ('False')
    
def main():
    n = int(input('Digite um número, se ele for ímpar, voltará true, se for par voltará false'))
    print(impar(n))

if __name__ == '__main__':
    main()