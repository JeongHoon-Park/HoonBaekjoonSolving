#가장 긴 증가하는 부분수열 Longest Increasing Sub-Sequence LSI
#DP Use Memoization O(n^2)
import sys
getInput = lambda : sys.stdin.readline().strip()
memo = [-1 for _ in range(1001)]

#인풋 받음
size= int(getInput())
seq = list(map(int, getInput().split()))

def maxR(par1, par2):
  if(par1<par2):
    return par2
  else:
    return par1

def solve(start):#solve함수를 start에서 시작하는 가장 긴 부분수열의 길이로 정의
  ret = memo[start]
  if(ret>-1): return ret
  ret = 1
  for index in range(start+1, size):
    if(seq[start]<seq[index]):
      ret = maxR(ret, solve(index)+1)
  memo[start]=ret
  return ret

maxLength = 0
for startIndex in range(size):#startIndex부터 시작하는 가장 긴 부분수열의 길이
  maxLength = maxR(maxLength, solve(startIndex))
print(maxLength)