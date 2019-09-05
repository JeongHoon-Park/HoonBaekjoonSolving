import sys
get_input = lambda : map(int, sys.stdin.readline().split())
constant = 9999999
#도시 N개 [1, 300]
#도시는 M개 이하로 지남
#항로는 K개 주어지고 출발점 -> 도착점 기내식 점수로 주어짐
#이때 기내식 점수가 최대가 되게 지나가야한다.
#N, M, K
city, via, way = get_input()#map(int, input().split())
#1번 도시부터 city 도시까지

#항로저장
score = []
highScore_many=[]#목적지까지, 몇 번을 거쳐서
for num in range(city+1):
  tempL = [-1 for _ in range(city+1)]
  score.append(tempL)#score가 -1이 아니면 항로가 있고, 기내식 점수
  exitL = [-1 for _ in range(via+1)]
  highScore_many.append(exitL)

#기내식 점수 인풋받았다
for ind in range(way):
  start, end, scoreF = get_input()
  if(scoreF>score[start][end]):
    score[start][end] = scoreF #score에는 end->start까지

#print(score)
#이 도시에 도착하기까지 가장 높은 점수와 경유 횟수
#highScore_many[1][1]=0

def set_max_score(arrive, visit):
#arrive에 도착하기까지 visit번 방문하면서 최대 기내식 점수
#  print(highScore_many)
  if(visit==via and arrive!=city):
    return -constant
  if(arrive==city):
    return 0
  ret = highScore_many[arrive][visit]
  if(ret!=-1):
    return ret
  ret=0
  for end in range(arrive+1, city+1):
    if(score[arrive][end]!=-1): #경로 있음
#      print('start : '+str(arrive)+' end: '+str(end))
      ret = max(ret, score[arrive][end]+set_max_score(end, visit+1))
      highScore_many[arrive][visit]=ret
  return ret

print(set_max_score(1,1))