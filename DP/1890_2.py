import sys
get_input = lambda : list(map(int, sys.stdin.readline().split()))

plate_size = int(input())
plate = []
memo = [[-1]*plate_size for _ in range(plate_size)]
for i in range(plate_size):
  plate.append(get_input())

def way_from_here(row, col):
  if(row==plate_size-1 and col==plate_size-1):
    return 1
  
  how_many_way = memo[row][col]
  if(how_many_way!=-1):
    return how_many_way

  how_many_way=0
  jump = plate[row][col]
  if((row+jump)<plate_size and jump!=0):
    how_many_way += way_from_here(row+jump, col)
  if((col+jump)<plate_size and jump!=0):
    how_many_way += way_from_here(row, col+jump)

  memo[row][col] = how_many_way
  return how_many_way

print(way_from_here(0,0))