#test case 개수
test = int(input())
#걍 50 by 50 으로 plate 하나 만들어버리기
plate=[]
for i in range(50):
    tempL=[]
    for j in range(50):
        tempL.append(0)
    plate.append(tempL)
#여기에다가 답 저장 할 거야
answer = []
#이거는 이동할 때 쓰는 배열이야
move = [[0, 1], [1, 0], [0, -1], [-1, 0]]#right, down, left, up

def DFS(indX, indY, maxX, maxY):
    stack = [[indX, indY]]
    plate[indX][indY] -= 1 #stack에 넣을때 방문했다는 표시로 1을 빼주자.
    while(stack):
        curX, curY = stack.pop(0)
        for d in move:
            tempX = curX + d[0]
            tempY = curY + d[1]
            if(tempX>=0 and tempX<maxX and tempY>=0 and tempY<maxY and plate[tempX][tempY]):
                stack.append([tempX, tempY])
                plate[tempX][tempY] -= 1  #역시 마찬가지로 넣을 때 1 빼줌
                #배추 있는 곳을 다 방문했다면 plate 전체가 0이 되야한다.

while(test>0):
    x, y, cabbage = map(int, input().split()) #가로, 세로, 배추개수
    for i in range(cabbage): #배추 위치 받음
        cabX, cabY = map(int, input().split())
        plate[cabX][cabY] = 1
    tempN = 0
    for i in range(50):
        for j in range(50):
            if(plate[i][j] == 1):
                DFS(i, j, x, y)
                tempN += 1      
    answer.append(tempN)    
    #TEST 개수 줄임
    test -= 1

for i in answer:
    print(i)