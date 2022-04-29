from email import message
from locale import DAY_1
from this import d

def data(a, b, c):
    

def niver(d, m, a):




def main():
    dia = int(input('que dia estamos ?'))
    mes = int(input('que mês estamos ?'))
    ano = int(input('que ano estamos ?'))

    dia_nascimento = int(input('Em que você nasceu ?'))
    mes_nascimento = int(input('Em que você nasceu ?'))
    ano_nascimento = int(input('Em que você nasceu ?'))

    d1, d2, d3 = data(dia, mes, ano)

    a1, a2, a3 = niver(dia_nascimento, mes_nascimento, ano_nascimento)

    if __name__ == "__main__":
        main()