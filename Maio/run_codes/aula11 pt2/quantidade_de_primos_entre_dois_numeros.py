def n_primos(x):
    divisiveis = 0
    for i in range(1, (x + 1)):
        if x % i == 0:
            divisiveis += 1
    return (divisiveis)

def main():

 numero = int(input())

 print(n_primos(numero))

if __name__ == "__main__":
     main()

