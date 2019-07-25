import sys
inpCom = int(input())
inpEdge = input()

#Getting Input
inpL = []
for i in sys.stdin.readlines(): #ReadLine Input need EOF
    tempL = i.split()

    tempL = [int(s) for s in i.split()] #list comprehension

    inpL.append(tempL)

#Setting Plate for saving data
plateL=[]
for i in range(0, inpCom+1):
    plateL.append(0)

def checkRoute(startIndex):
    plateL[startIndex] += 1
    if(plateL[startIndex]>=2): #plateL[z]가 두 번 이상 체크 되있다는 건 한 번 확인했다는 뜻이므로 리턴
        return
    for i in range(0, len(inpL)):
        if(inpL[i][0]==startIndex): # x<->y 에서 x가 startIndex일 때
            checkRoute(inpL[i][1])
        if(inpL[i][1] == startIndex): # x<->y 에서 y가 startIndex일 때
            checkRoute(inpL[i][0])
checkRoute(1)

tempC = -1
for i in range(0, len(plateL)):
    if(plateL[i] > 0):
        tempC += 1
print(tempC)

