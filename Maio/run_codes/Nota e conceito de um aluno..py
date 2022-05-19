chama = True #variável que padroniza seu valor como true
while chama == True: #enquanto a variável while tiver valor true, seu bloco será executado.
        nota = float(input('Digite sua nota: '))
        if 8.5 <= nota <=10:
            print('A')
            chama = False #todas as linhas como essa tem a função de parar a execução do bloco, pois muda o valor da variável "chama" para false.
        elif nota >= 7.0 and nota < 8.5:
            print('B')
            chama = False
        elif 5.0 <= nota < 7.0:
            print('C')
            chama = False
        elif 4.0 <= nota < 5.0:
            print('D')
            chama = False
        elif 0 <= nota < 4.0:
            print('E')
            chama = False
        else: 
            print('Nota inválida')
            chama = True  #Essa é diferente pois retorna True, condição para que o bloco seja inciado, o que é  necessário depois que um valor inválido foi indicado. 
print('FIM')
