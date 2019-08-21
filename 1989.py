#리스트를 받아서 리턴
def maxScore(par1, par2):
  if(par1[0]<par2[0]):
    return par2
  else:
    return par1

def min(par1, par2):
  if(par1<par2):
    return par1
  else:
    return par2

panjaL = []

#문제를 풉시다
def solve(left, right):#left<= x <=right 범위 안에서 최댓값이 있다면 출력
  if(left==right):
    return [panjaL[left]*panjaL[left], left, left]
  mid = (left+right)//2
  #case 1,2 : 중간의 왼쪽에 최대값이 있을 때, 오른쪽에 최대값이 있을 때
  ret = maxScore(solve(left, mid), solve(mid+1, right))
  #case 3 중간에서 최대값이 있을 때
  #decrement 감소 increment 증가
  dec = mid
  inc = mid+1
  minHei = min(panjaL[dec], panjaL[inc])
  length = panjaL[dec]+panjaL[inc]
  while(left<dec or inc<right): #중간에서부터 한칸씩 늘려가며 최대 넓이 찾기
    if(inc<right and (dec==left or panjaL[dec-1]<panjaL[inc+1])):
      inc+=1
      minHei = min(panjaL[inc], minHei)
      length += panjaL[inc]
    else:
      dec-=1
      minHei = min(panjaL[dec], minHei)
      length += panjaL[dec]
    ret = maxScore(ret, [minHei*length, dec, inc])
  return ret

#인풋 받읍시다
panja = int(input())
panjaL = list(map(int, input().split()))
answer = solve(0, panja-1)
print(answer[0])
print(str(answer[1]+1)+' '+str(answer[2]+1))