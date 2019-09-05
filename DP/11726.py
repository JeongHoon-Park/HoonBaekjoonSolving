import sys
sys.setrecursionlimit(1500)

constant = 10007
width = int(input())
memo = [-1 for _ in range(width+2)]
memo[0]=1
memo[1]=1

def solve(size):
  ret = memo[size]
  if(ret>-1):
    return ret
  ret = (solve(size-1)+solve(size-2)+constant)%constant
  memo[size] = ret
  return ret

print(solve(width))