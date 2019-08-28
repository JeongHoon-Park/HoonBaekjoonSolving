constant = 1000000
password = input()
password = list(map(int, password))
password.insert(0, -1)
lenPassword = len(password)#원래 암호 길이 +1

memo = [-1 for _ in range(lenPassword+1)]

memo[0]=1
memo[1]=1
def solve(index):#시작 인덱스 2부터 시작하도록
  ret = memo[index]
  if(ret!=-1):
    return ret
  ret = 0
  if(password[index]>0):
    ret = solve(index-1)%constant
  temp = password[index-1]*10+password[index]
  if(temp>=10 and temp<=26):  
    ret = (ret+solve(index-2))%constant
  memo[index]=ret

if(password[1]==0):
  print(0)
else:
  for size in range(2, lenPassword):
    solve(size)
  print(memo[lenPassword-1])