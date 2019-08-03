import sys
inpN = int(input())
heap = [0, 1]
if(inpN==1): #1들어오면 그냥 끝냄
    print(heap[1])
    sys.exit()

def change(index1, index2): #바꿔주는 함수
    temp = heap[index2]
    heap[index2] = heap[index1]
    heap[index1]=temp

for i in range(2, inpN+1):
    heap.append(i)
    change(i-1, i)  #맨 뒤에 최댓값 넣고 그 앞이 1이니까 자리 바꿔줌
    maxIndex = i-1
    while(maxIndex>1):  #최대힙을 유지해주는 과정
        change(maxIndex//2, maxIndex)   #최댓값이 있는 위치에서 위로 올라감
        maxIndex//=2

for i in range(1, inpN+1):
    print(heap[i], end=" ")