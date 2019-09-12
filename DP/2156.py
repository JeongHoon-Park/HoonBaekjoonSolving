import sys
get_input = lambda : int(sys.stdin.readline().strip())

#인풋 받고 처리
wine_cup = get_input()
wine = []
memo = []
for i in range(wine_cup):
  wine.append(get_input())
  memo.append([-1]*3) #memo[wine_cup, end_drink]
wine.insert(0, 0)
memo.insert(0, [-1, -1, -1])

memo[1][1] = wine[1]
memo[1][0] = 0

for index in range(2, wine_cup+1):
  memo[index][2] = memo[index-1][1]+wine[index]
  memo[index][1] = memo[index-1][0]+wine[index]
  temp_max = max(memo[index-1][2], memo[index-1][1])
  temp_max = max(temp_max, memo[index-1][0])
  memo[index][0] = temp_max

max_wine = 0
for temp_max in memo[wine_cup]:
  if(temp_max>max_wine):
    max_wine = temp_max
print(max_wine)