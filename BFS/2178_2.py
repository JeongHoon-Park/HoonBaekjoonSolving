
plate = []
height, width = map(int, input().split())
for i in range(height):
    tempL = list(map(int, input()))
    plate.append(tempL)

def solve(start, goal):

    que = []
    que.append(start)

    dx = [-1, 0, 1, 0]  #up, right, down, left
    dy = [0, 1, 0, -1]

    while que: 
        x, y = que.pop(0)
        depth = plate[x][y]

        for i in range(4):
            temp_x = x + dx[i]
            temp_y = y + dy[i]
            #범위 밖
            if(temp_x < 0 or temp_y <0 or temp_x >= height or temp_y >= width):
                continue
            #벽
            temp_depth = plate[temp_x][temp_y]
            if(temp_depth < 1):
                continue
            
            #더 작은 depth 가 있을 때
            if(temp_depth == 1 or temp_depth > depth+1):
                plate[temp_x][temp_y] = depth + 1
                que.append([temp_x, temp_y])

    return plate[goal[0]][goal[1]]

print(solve([0, 0], [height-1, width-1]))