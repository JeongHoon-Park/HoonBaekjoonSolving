import sys
get_input = lambda : list(map(int, sys.stdin.readline().split()))

#get input
plate_size = int(input())
plate = []
memo = [[0]*plate_size for _ in range(plate_size)]
for i in range(plate_size):
  plate.append(get_input())

#현재 자리에서 경로 탐색
def way_from_here(row, col, before):
  #print('row : '+str(row)+' col : '+str(col))
  if(row==(plate_size-1) and col==(plate_size-1)):
    memo[row][col] += before
    return
  #현재 위치까지 올 수 있는 경로 수
  memo[row][col] += before
  jump = plate[row][col]
  if(jump==0):
    return
  how_many_way = memo[row][col]
  if((row+jump)<plate_size):
    way_from_here(row+jump, col, how_many_way)
  if((col+jump)<plate_size):
    way_from_here(row, col+jump, how_many_way)

way_from_here(0,0,1)
print(memo[plate_size-1][plate_size-1])