import sys
get_input = lambda : map(int, sys.stdin.readline().split())
city, via, way = get_input()

score = []
highScore_many=[]
score = [[-1]*(city+1) for _ in range(city+1)]
highScore_many = [[-1]*(via+1) for _ in range(city+1)]

for ind in range(way):
  start, end, scoreF = get_input()
  if(scoreF>score[start][end]):
    score[start][end] = scoreF

for dest in range(2, city+1):
  if(score[1][dest]!=-1):
    highScore_many[dest][2] = score[1][dest]
for start in range(2, city):
  for visit in range(2, via):
    for dest in range(start+1, city+1):
      if(score[start][dest]!=-1 and highScore_many[start][visit]!=-1):
        highScore_many[dest][visit+1]= max(highScore_many[dest][visit+1], score[start][dest]+highScore_many[start][visit])

print(max(highScore_many[city]))