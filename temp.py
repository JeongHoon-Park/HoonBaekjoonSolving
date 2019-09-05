import random
fw = open('test.txt', 'wt')

for i in range(1000):
  fw.write(str(random.randint(1, 1000))+' ')
