#인풋을 받자.
inpN = int(input())
inpP = []
for i in range(inpN):
    tempL = list(int(s) for s in input())
    inpP.append(tempL)

# 여기에는 답을 담을거야. 각 단지에 몇 개의 집이 있는지
answerL = []

move = [[0, 1], [0, -1], [1, 0], [-1, 0]] #Right Left Down Up

def DFS(indX, indY):
    stack = [[indX, indY]]
    num = 1
    while(stack):
        tempI = stack.pop(0)
        for p in move:
            tempX = tempI[0]+p[0]
            tempY = tempI[1]+p[1]
            if(tempX<0 or tempX>=inpN or tempY<0 or tempY>=inpN):
                continue #배열 index 밖으로 나가면 넘기자
            if(inpP[tempX][tempY]==1):
                stack.append([tempX, tempY])
                inpP[tempX][tempY] += 1
                num += 1
                #방문한 적이 없다면 스택에 푸시
    answerL.append(num)#DFS 끝내고 집 갯수 리스트에 추가

#이중 포문으로 돌리면서 일일이 찾아본 다음 방문 안 한 집이 있으면 푸시
#거기에서 DFS
#방문 안 한 집은 1
#방문 할 때 마다 1씩 추가
for i in range(inpN):
    for j in range(inpN):
        if(inpP[i][j]==1):
            #여기서 DFS
            inpP[i][j] += 1
            DFS(i, j)

#정답 출력
answerL.sort()
print(len(answerL))
for i in answerL:
    print(i)