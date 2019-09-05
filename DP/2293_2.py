import sys

N,K = map(int,sys.stdin.readline().split())
coins = []
for n in range(N):
    coins.append(int(sys.stdin.readline()))

#DP 초기화
dp = [0 for _ in range(K+1)]
dp[0] = 1

for value in coins:
    for k in range(value,K+1):
        dp[k] += dp[k-value]
#작은 단위 동전부터 차근차근, 원하는 가격을 만들 수 있는지
#전 수에다가 그 가치의 동전이 있으면 더해서 1가지 경우를 추가
print(dp[K])