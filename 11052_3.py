cardWanted = int(input())
packPrice = [0] + list(map(int, input().split()))

memo = [0 for _ in range(cardWanted+1)]

for i in range(1, cardWanted+1):
  for j in range(1, i+1):
    memo[i] = max(memo[i], packPrice[j]+memo[i-j])
print(memo[cardWanted])