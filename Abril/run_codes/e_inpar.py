def impar(x):
    if x % 2 == '1':
      print ('True')
    else:
     print ('False')
    
def main():
    n = int(input())
    print(impar(n))

if __name__ == '__main__':
    main()