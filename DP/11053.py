#가장 긴 증가하는 부분수열 Longest Increasing Sub-Sequence LSI
#BruteForce O(n^2)
import sys
getInput = lambda : sys.stdin.readline().strip()

#인풋 받음
size= int(getInput())
seq = list(map(int, getInput().split()))

def maxR(par1, par2):
  if(par1<par2):
    return par2
  else:
    return par1

#일단 완전탐색으로 O(n^2)
def brute_force(number_list):
  list_len = len(number_list)
  if(list_len==0):
    return 0

  ret = 0
  for start in range(list_len):
    #배열 돌면서 일일이 탐색
    next_list = []
    for nextI in range(start+1, list_len):
      if(number_list[start]<number_list[nextI]):
        #start 할 때의 수보다 큰 수는 모두 푸시
        next_list.append(number_list[nextI])
    #재귀적으로 끝에서부터 탐색 i+1번째부터 큰 수열의 정보를 그대로 가져와
    #i번째부터 큰 수열의 정보를 탐색하는데 사용
    #그렇다면 i+1번째 수열보다 크고, i번째 수열보다도 큰 수열이 남게된다.
    ret = maxR(ret, brute_force(next_list)+1)
  return ret

print(brute_force(seq))