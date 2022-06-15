metros_a_frente = int(input('Em quantos metros a tartaruga começa na frente da lebre? '))
posicao_tartaruga = metros_a_frente
posicao_lebre = 0
minutos = 0

while posicao_lebre < posicao_tartaruga: #enquanto a posição da lebre for menor que o da tartaruga, o bloco será executado. 
    posicao_tartaruga += 1 #a cada laço a tartarua corre 1 metro.
    posicao_lebre += 10 # a cada laço a lebre corre 10 metros
    minutos += 1 #cada laço e igual a um minuto

print('Demorará {} minutos para a lebre alcançar a tartaruga.'.format(minutos))