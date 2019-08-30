import sys
get_input = lambda : map(int, sys.stdin.readline().split())
#도시 N개 [1, 300]
#도시는 M개 이하로 지남
#항로는 K개 주어지고 출발점 -> 도착점 기내식 점수로 주어짐
#이때 기내식 점수가 최대가 되게 지나가야한다.

#N, M, K
city, via, way = get_input()#map(int, input().split())
#1번 도시부터 city 도시까지

#항로저장
score = []
highScore_many=[]
for num in range(city+1):
  tempL = [-1 for _ in range(city+1)]
  score.append(tempL)#score가 -1이 아니면 항로가 있고, 기내식 점수
  highScore_many.append(tempL)

#기내식 점수 인풋받았다
for ind in range(way):
  start, end, scoreF = get_input()
  if(scoreF>score[start][end]):
    score[start][end] = scoreF #score에는 end->start까지

#이 도시에 도착하기까지 가장 높은 점수와 경유 횟수
highScore_many[1][1]=0

def saveScore(end, visit):
  #지금까지 들른 도시 수가 K보다 작고
  if((visit+1)==via and end!=city):
    return -1
  if(end==city):
    return 0
  
  ret = highScore_many[end][visit]
  if(ret!=-1):
    return ret
  #이제 highScore_many[end][visit]을 구해야해
  for arrive in range(end+1, city+1):
    if(score[end][arrive]!=-1):
      ret = max(ret, saveScore(arrive, visit+1)-score[end][arrive])
      highScore_many[end][visit]=ret
  return ret

saveScore(1, 1)
tempMax = -1
for i in range(1, via+1):
  tempMax = max(tempMax, highScore_many[city][i])
print(tempMax)