#Baekjoon Fibonachi Function

#use DP - memoization

#0을 부르는 횟수와 1을 부르는 횟수를 memoization 합니다.
callNum0 = []
callNum1 = []
for i in range(41):#초기화는 -1로 합니다.
  callNum0.append(-1)
  callNum1.append(-1)

callNum0[0] = 1 #fibonacci(0)은 0을 1번 호출합니다.
callNum1[0] = 0 #fibibaccu(1)은 1을 0번 호출합니다.
callNum0[1] = 0
callNum1[1] = 1

#0을 몇 번 부르는지 계산합니다.
def howManyCall0(input):
  if(callNum0[input]>=0):
    return callNum0[input]
  else:
    callNum0[input] = howManyCall0(input-1)+howManyCall0(input-2)
    return callNum0[input]

#1을 몇 번 부르는지 계산합니다.
def howManyCall1(input):
  if(callNum1[input]>=0):
    return callNum1[input]
  else:
    callNum1[input] = howManyCall1(input-1)+howManyCall1(input-2)
    return callNum1[input]

cases = int(input())
while cases:
  inp = int(input())
  print(str(howManyCall0(inp))+' '+str(howManyCall1(inp)))
  cases -= 1