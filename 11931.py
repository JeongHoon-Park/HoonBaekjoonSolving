
#Count Sort
inpN = int(input())

#Set Plate
plate = []
for i in range(0, 2000001):
    plate.append(0)

#Getting Input
for i in range(0, inpN):
    tempN = int(input())
    plate[tempN+1000000]=1

#print Sorted Output
for i in range(2000000, -1, -1):
    if(plate[i]):
        print(i-1000000)