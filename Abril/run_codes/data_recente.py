
dia_atual = int(input())
mes_atual = int(input())
ano_atual = int(input())
qualquer_dia = int(input())
qualquer_mes = int(input())
qualquer_ano = int(input())

if ano_atual > qualquer_ano or mes_atual > qualquer_mes or dia_atual > qualquer_dia:
    print(dia_atual,mes_atual,ano_atual, sep='/')
else:
    print(qualquer_dia,qualquer_mes,qualquer_ano, sep='/')