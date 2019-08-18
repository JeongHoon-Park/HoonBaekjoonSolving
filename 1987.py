hei, wid = map(int, input().split())
plate = []
#어차피 스트링이니까 그냥 인풋 받아서 넣어버리면 된다링
for i in range(hei):
    tempL = input()
    plate.append(tempL)

#이동하는 값
dXY = [[0, 1], [1, 0], [0, -1], [-1, 0]]

#알파벳을 만난적이 있는지 바로 체크할거임
visit = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0,
            'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0,
            'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
#스택 쌓을거
stack = [[0,0,1]]
#답
max_answer = 0

while(stack):
    indX, indY, depth= stack.pop()
    print('indX, indY : '+str(indX)+' '+str(indY))
    if(depth>max_answer):
        max_answer = depth
    if(not(plate[indX][indY] in visit)):
        visit[plate[indX][indY]] = 1
    for d in dXY:
        tempX = indX + d[0]
        tempY = indY + d[1]
        if(tempX<0 or tempX>=hei or tempY<0 or tempY>=wid):
            continue
        if(plate[tempX][tempY] in visit):
            continue
        stack.append([tempX, tempY, depth+1])
        print('tempX, tempY : '+str(tempX)+' '+str(tempY))

print(max_answer)
#지나온 경로만을 표시해야한다
#(0, 0) (0,1) 그리고 그 경로상에서 있었던 방문 알파벳만 검사해야한다
def DFS(visit):
    if(not(stack)):
        return
    indX, indY, depth= stack.pop()
    
    #간 경로에 따라 visit을 구성하는 것이 가장 중요해 depth에 따라 구성해야 할듯

    #유효한 방문지들이 있으면 stack에 넣고 아니면 depth를 리턴
    valid_dest = isValid(indX, indY)
    if(valid_dest):
        for d in valie_dest:
            stack.append([d[0], d[1], depth+1])
    else:
        #리턴하든가 말든가

#네가지 방향으로 방문해보고 갈 곳이 있으면 배열을 반환
#없으면 false 반환
def isValid(indX, indY):
    tempL = []
    for d in dXY:
        tempX = indX + d[0]
        tempY = indY + d[y]
        if(tempX<0 or tempX>=hei or tempY<0 or tempY>=wid):
            continue
        if(plate[tempX][tempY] in visit):
            continue
        tempL.append([tempX, tempY])
    if(tempL):
        return tempL
    else:
        return False