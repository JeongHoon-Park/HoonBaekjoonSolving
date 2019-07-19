#getting input
caseNum = int(input())
caseL = []
for i in range(0, caseNum):
    caseL.append(int(input()))

#삼각수를 가지고 있는 배열 하나 만들기 44개까지 왜냐하면 44번째 삼각수가 990
triL = [1]
for i in range(2, 45):
    triL.append(triL[i-2]+i)

#Ready for Plate
all_possible_list = []
for i in range(0, 1000):
    all_possible_list.append(0)

#Set All Possible Cases
for i in range(0, 44):
    for j in range(0, 44):
        for k in range(0, 44):
            tempNum = triL[i]+triL[j]+triL[k]-1
            if(tempNum>999):
                continue
            if(all_possible_list[tempNum]==0):
                all_possible_list[tempNum]=1

#print the answer
for i in range(0, len(caseL)):
    print(all_possible_list[(caseL[i]-1)])