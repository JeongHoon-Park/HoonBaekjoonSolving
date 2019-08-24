#동전으로 k원을 낼 수 있는 경우의 수
#N(i, k) => i까지의 동전을 가지고 k원을 낼 수 있는 동전 경우의 수
#N(i, k) = N(i-1, k)  (C(i)>k)
#N(i, k) = N(i-1, k)+N(i, k-C(i)) (C(i)<=k)
import sys
getInput = lambda : sys.stdin.readline().strip()

#unit : 동전 단위 종류, goal : 이것으로 얼마를 만들 것인지.
unit, goal = map(int, getInput().split())

#memo 하기 위한 판을 만드는 거임.
memo = []
for j in range(2):
  tempL=[]
  for i in range(goal+1):
    tempL.append(-1)
  memo.append(tempL)

#unitL : 동전 단위 저장
unitL = []
for _ in range(unit):
  unitL.append(int(getInput())) 

def solve(goal):
  for value in range(goal+1):
    if(value%unitL[0]==0):
      memo[0][value]=1
    else:
      memo[0][value]=0
  for coin in range(1, unit):#unit : coin 갯수
    for value in range(goal+1):#value : 만들고자 하는 돈 가치
      if(coin%2==0):
        if(unitL[coin] > value): #N(i,k) = N(i-1, k) (C(i)>k)
          memo[0][value]=memo[1][value]
        else:#N(i,k) = N(i-1, k) + N(i, k-C(i)) (C(i)<=k) (coin<=value)
          memo[0][value]= memo[1][value]+memo[0][value-unitL[coin]]      
      else:
        if(unitL[coin] > value): #N(i,k) = N(i-1, k) (C(i)>k)
          memo[1][value]=memo[0][value]
        else:#N(i,k) = N(i-1, k) + N(i, k-C(i)) (C(i)<=k) (coin<=value)
          memo[1][value]= memo[0][value]+memo[1][value-unitL[coin]]
  return memo[(unit-1)%2][goal]

print(solve(goal))