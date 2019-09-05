#최대 직사각형 넓이
#테스트 케이스 수 50이하
#판자 수 20000이하
#판자 높이 10000이하

#작은 거 리턴하는 함수
def max(par1, par2):
  if(par1<par2):
    return par2
  else:
    return par1

def min(par1, par2):
  if(par1<par2):
    return par1
  else:
    return par2
    
#문제를 풉시다
def solve(left, right, panjaL):#left<= x <=right 범위 안에서 최댓값이 있다면 출력
  if(left==right):
    return panjaL[left]
  mid = (left+right)//2
  #case 1,2 : 중간의 왼쪽에 최대값이 있을 때, 오른쪽에 최대값이 있을 때
  ret = max(solve(left, mid, panjaL), solve(mid+1, right, panjaL))
  #case 3 중간에서 최대값이 있을 때
  #decrement 감소 increment 증가
  dec = mid
  inc = mid+1
  minHei = min(panjaL[dec], panjaL[inc])
  while(left<dec or inc<right): #중간에서부터 한칸씩 늘려가며 최대 넓이 찾기
    if(inc<right and (dec==left or panjaL[dec-1]<panjaL[inc+1])):
      inc+=1
      minHei = min(panjaL[inc], minHei)
    else:
      dec-=1
      minHei = min(panjaL[dec], minHei)
    ret = max(ret, minHei*(inc-dec+1))
  return ret

###
#인풋 받읍시다.
cases = int(input())

while cases:
  panja = int(input())
  height = list(map(int, input().split()))
  print(solve(0, panja-1, height))
  cases -=1
