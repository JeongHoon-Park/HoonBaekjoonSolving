inp = input()
inp = inp.split()
inpX = int(inp[0])
inpY = int(inp[1])
inpP = []

#get Chess input
for x in range(0, inpX):
    temp=input()
    tempL = []
    for y in range(0, len(temp)):
        if(temp[y]=='W'):
            tempL.append(1)
        else:
            tempL.append(0)
    inpP.append(tempL)

#set correct plate
plate1 = [[1, 0, 1, 0, 1, 0, 1, 0],[0, 1, 0, 1, 0, 1, 0, 1],[1, 0, 1, 0, 1, 0, 1, 0],[0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1]]
plate2 = [[0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0],[0, 1, 0, 1, 0, 1, 0, 1],[1, 0, 1, 0, 1, 0, 1, 0],[0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0]]

#Find How many cell needed to redraw on each possible case
startPX = 0
startPY = 0
redrawL = []
for startPX in range(0, inpX-7):
    for startPY in range(0, inpY-7):
        redraw1 = 0
        redraw2 = 0
        for x in range(0, 8):
            for y in range(0, 8):
                if(inpP[startPX+x][startPY+y]!=plate2[x][y]):
                    redraw2 += 1
                if(inpP[startPX+x][startPY+y]!=plate1[x][y]):
                    redraw1 += 1
        if(redraw1<redraw2):
            redrawL.append(redraw1)
        else:
            redrawL.append(redraw2)

#find the smalletst case
redraw = 100
for x in range(0, len(redrawL)):
    if(redrawL[x]<redraw):
        redraw = redrawL[x]
print(redraw)
