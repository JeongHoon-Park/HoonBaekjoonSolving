cardWanted = int(input())
packPrice = list(map(int, input().split()))
packPrice.insert(0, -1)

memo = [-1 for _ in range(cardWanted+1)]#i번째 카드까지 뽑을 때 최대가격

def returnPrice(index):
  if(memo[index]!=-1):
    return memo[index]
  else:
    return 0

for i in range(1, cardWanted+1):
  #빼고 남는 수로 또 함수 돌림
  for j in range(1, i+1):
    ret = returnPrice(i)
    ret = max(ret, packPrice[j]+returnPrice(i-j))
    memo[i] = ret

print(memo[cardWanted])