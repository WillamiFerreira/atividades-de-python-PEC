populacao_total = int(input('Número da popução de dodôs no inicio de 1600: '))
dezporcento = 10/100 * populacao_total #variável que funciona como flag, pois define os 10% do total da poppulação.
#três inicializadores
nascidos = 0
mortes = 0
ano = 1600

while populacao_total >= dezporcento: # enquanto o total de dodôs do começo do ano for maior que 10% do começo do ano de 1600, o bloco será executado.
    nascidos = 1/100 * populacao_total #no final de cada ano, nasce o cerrespondente a 1% do total de dodôs do começo no mesmo ano.
    mortes = 6/100 * populacao_total # no final de cada ano, morre o correspondente a 6% do total de dodôs do começo do mesmo ano.
    populacao_total += nascidos - mortes #depois que o número de mortes e nascimentos totais do ano foram calculados e armazenados, o total da população daquele ano pode ser calculado, somando a população já existente os narcidos no ano e subtraindo os mortos do ano.
    print(f'{ano},{nascidos:.0f},{mortes:.0f},{populacao_total:.0f}') #impressão formatadas dos dados de cada ano.
    ano += 1
    