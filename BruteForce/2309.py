inputArr = []
sum = 0
interimSum = 0
interimSum2 = 0
for x in range(0, 9):
    inputArr.append(int(input()))
    sum+=inputArr[x]
inputArr.sort()

for x in range(0, 9):
    interimSum = sum
    interimSum -= inputArr[x]
    for y in range(x+1, 9):
        interimSum2 = interimSum
        interimSum2 -= inputArr[y]
        if(interimSum2 == 100):
            break
    if(interimSum2 == 100):
        break

for z in range(0,9):
    if(z==x or z==y):
        continue
    print(inputArr[z])