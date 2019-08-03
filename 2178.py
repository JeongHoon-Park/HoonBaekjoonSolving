x, y = map(int,input().split())

#Getting Input
plateL = []
for i in range(x): #Readline Input
    tempL = list(map(int, input()))
    plateL.append(tempL)

#Setting Queue
q = [[0,0, 0]]

#push
def push(indx, indy, depth):
    #push 할 때 선별적으로 push
    if(indx<0 or indy<0 or indx>=x or indy>=y): #탐색 범위 밖으로 벗어났을 때
        return
    if(depthL[indx][indy] <= depth):
        return    
    if(plateL[indx][indy]):
        q.append([indx, indy, depth])

#최소 depth 저장하는 다른 plate가 필요하다.
depthL = []
for i in range(0, x):
    tempL = []
    for j in range(0, y):
        tempL.append(10010)
    depthL.append(tempL)

#갈 수 있는 경로의 index를 넣는다.
#뺀다. 그 경로에서 갈 수 있는 index를 넣는다.
#이 과정을 반복하면서 depth를 표시한다.
while(True):
    indx, indy, depth = q.pop(0)    #ind[0] = indx , ind[1] = indy, ind[2] = depth

    if(depthL[indx][indy] > depth):
        depthL[indx][indy] = depth

    if(indx == (x-1) and indy == (y-1)):
        #answer
        print(depth+1)
        break
    
    #갈 수 있는 경로의 index를 queue에 넣는다.
    push(indx-1, indy, depth+1)
    push(indx+1, indy, depth+1) 
    push(indx, indy-1, depth+1)
    push(indx, indy+1, depth+1)
