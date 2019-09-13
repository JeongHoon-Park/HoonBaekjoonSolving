import sys
get_input = lambda : int(sys.stdin.readline().strip())

already_have, required = map(int, input().split())

line_length=[]
for i in range(already_have):
    line_length.append(get_input())

line_length.sort(reverse=True)
max_line = line_length[0]+10

def return_possible_line_with(sample):
    tempSum = 0
    for line in line_length:
        tempSum += line//sample
    return tempSum

def find_longest_line_length(upper, down):
    if((upper-1)<=down):
        return down
    
    mid = (upper+down)//2
    
    if(required>return_possible_line_with(mid)):
        ret = find_longest_line_length(mid, down)
    else:
        ret = find_longest_line_length(upper, mid)
    return ret

if(required==1):
    print(line_length[0])
    sys.exit()
else:
    print(find_longest_line_length(max_line, 1))