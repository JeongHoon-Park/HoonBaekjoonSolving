#N개의 카드를 구매하려고 한다.
#Pi 카드팩에는 i개의 카드가 들어있다.
#이때 가장 많은 돈을 지불하도록 카드팩을 산다.

cardWanted = int(input())
packPrice = list(map(int, input().split()))
packPrice.insert(0, -1)
answer = 0 #max total price
memo = [[-1]*(cardWanted+1) for _ in range(cardWanted+1)] #for memoization (packLimit, moreWantedCard)

#함수에 써야할 카드팩 한계랑 더 뽑아야하는 카드 수를 매개변수로 준다.
def returnSubMaxPrice(packLimit, moreWantedCard):
  maxSubSum = 0
  moreCard = moreWantedCard
  if(moreCard <= 0 or packLimit>cardWanted):
    return maxSubSum

  if(memo[packLimit][moreWantedCard]!=-1):
    return memo[packLimit][moreWantedCard]

  print('packLimit :  '+str(packLimit)+' moreWantedCard : '+str(moreWantedCard), end=' ')
  
  usingPackNumber = packLimit
  usingPackPrice = packPrice[usingPackNumber]
  curSum = 0

  #packLimit까지 팩을 사용하고 moreWantedCard만큼 카드를 뽑을 때 얻을 수 있는 최대합
  if(usingPackNumber <= moreWantedCard):
    while(usingPackNumber<=moreCard):
      moreCard -= usingPackNumber
      curSum += usingPackPrice
      #하나 하나 돌려가면서 확인
      maxSubSum = max(maxSubSum, curSum+returnSubMaxPrice(usingPackNumber+1, moreCard))
  else:
    maxSubSum = max(maxSubSum, curSum+returnSubMaxPrice(usingPackNumber+1, moreCard))

  memo[usingPackNumber][moreWantedCard] = maxSubSum
  print('maxSubSum : '+str(maxSubSum))
  return maxSubSum

#[(1, 1) (2, 2.5) (3, 2) (4, 1.75)]
#[(2, 2.5), (3, 2), (4, 1.75), (1, 1)]

print(returnSubMaxPrice(1, cardWanted))