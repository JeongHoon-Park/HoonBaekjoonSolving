#Get First Input
inpN, wanted= input().split()
wanted = int(wanted)
inpN = int(inpN)

#Get Second Input
inpL = input()
inpL = inpL.split()
for i in range(0, len(inpL)):
    inpL[i] = int(inpL[i])
plateTF = []
for i in range(0, inpN):
    plateTF.append(False)

#Set One plate
plate = []
for i in range(0,1000001):
    plate.append(0) #0, 1, 2, 3, ...

def subset(start, end):
    if(start>=end): #재귀함수 해제 조건
        mark()
        return
    else:
        changeTF(end-1, True) #맨끝을 true
        subset(start, end-1) #끝에서 하나씩 줄여가면서
        changeTF(end-1, False) #맨끝을 false
        subset(start, end-1)

def mark():
    tempSum = 0
    for i in range(0, inpN): #true 인 곳만 더해줌
        if(plateTF[i]):
            tempSum += inpL[i]
    if(wanted>=0): #원하는 수가 양수일 때와 음수일 대를 구별해서
        if(tempSum < 0 or tempSum>1000000): #1000000보다 크면 return 시키는 거 반드시 포함시켜야함
            return
        plate[tempSum] += 1
    else:
        if(tempSum >=0 or tempSum<-100000):
            return
        plate[-tempSum] += 1

def changeTF(index, TF):
    plateTF[index] = TF

subset(0, inpN)
if(wanted>=0):
    plate[0] -=1
    print(plate[wanted])
else:
    print(plate[-wanted])