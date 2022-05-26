tot_anos = 0
paisA = int(input())
paisB = int(input())

while paisA >= paisB:
    paisA += 2/100 * paisA
    paisB += 3/100 * paisB
    tot_anos += 1

print(tot_anos)