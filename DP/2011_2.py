# 1-A 2-B 3C 4-D 5-E 6-F 7-G 8-H 9-I 10-J
# 11-K 12-L 13-M 14-N 15-O 16-P 17-Q 18-R 19-S 20-T
#21-U 22-V 23-W 24-X 25-Y 26-Z

constant = 1000000
password = input()
password = list(map(int, password))
lenPassword = len(password)
password.insert(0, -1)

memo = [-1 for _ in range(lenPassword+1)]

#1자리 또는 2자리로 나누고 또 재귀함수 돌림
#두자리로 나눌때는 알파벳이 있을때만 더하고 아니면 걍 0을 리턴
#최대 값을 메모이제이션
memo[0]=1
memo[1]=1

#-1 2 5 1 1 4
def solve():#시작 인덱스, 끝나는 인덱스
  for index in range(2, lenPassword+1):      
    #ret = memo[start]
    #print(memo)
    ret = 0
    if(password[index]>0):
      ret = (memo[index-1]%constant)
      #memo[index-1]%constant
    if(index<lenPassword+1):
      temp = password[index-1]*10+password[index]
      if(temp>=10 and temp<=26):  
        ret = (ret + memo[index-2] + constant)%constant

    memo[index] = ret
  return memo[lenPassword]

if(password[1]==0):
  print(0)
else:
  print(solve())