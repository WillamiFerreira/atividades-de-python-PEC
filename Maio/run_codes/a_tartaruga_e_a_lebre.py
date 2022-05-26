metros_a_frente = float(input())
tartaruga_inicio = metros_a_frente
lebre_inicio = 0

minutos = 0
while lebre_inicio <= tartaruga_inicio:
    if tartaruga_inicio == 0:
        minutos = 0
        lebre_inicio += 10
        tartaruga_inicio += 1
    else:
        minutos += 1
        lebre_inicio += 10
        tartaruga_inicio += 1

print('{}'.format(minutos))