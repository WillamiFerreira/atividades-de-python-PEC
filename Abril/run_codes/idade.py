
dia = int(input())
mes = int(input())
ano = int(input())
dia_nascimento = int(input())
mes_nascimento = int(input())
ano_nascimento = int(input())
calculo = ano - ano_nascimento
if mes !=mes_nascimento or dia !=dia_nascimento:
    calculo -=1
    print(calculo)
else:
    print(calculo)
