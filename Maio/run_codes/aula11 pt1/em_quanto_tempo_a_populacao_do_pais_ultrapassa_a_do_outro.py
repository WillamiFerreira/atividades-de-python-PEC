paisA = int(input("População do país A: ")) 
paisB = int(input("População do País B: "))
anos = 0

if paisA > paisB: #se o país A tiver uma população maior, O bloco é executado.
    while paisA >= paisB:  #enquanto o paisA for maior ou igual ao paisB
        paisA += (2/100 * paisA) #país A a recebe + 2% de sua população daquele ano...
        paisB += (3/100 * paisB) #e o país B recebe + 3%
        anos += 1 #um ano é contado
    print(f'Será necessário {anos} anos para o pais B passar o país A.')
else: #esse bloco é automaticamente executado caso o if dê False. 
    while paisB >= paisA: 
        paisA += (3/100 * paisA)
        paisB += (2/100 * paisB)
        anos += 1
    
    print(f'será necessário {anos} anos para o país A passar o país B.')