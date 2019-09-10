import sys
get_input = lambda : sys.stdin.readline()

node_num = int(get_input())
parent_list = list(map(int, get_input().split()))
delete_node_index = int(get_input())

link_matrix =[]
link_matrix = [[-1]*node_num for _ in range(node_num)]
root = 0
for i in range(0, node_num):
  if(parent_list[i]==-1):
    root = i
    continue
  link_matrix[parent_list[i]][i] = 1

def delete_node(parent):
  for i in range(0, node_num):
    if(link_matrix[i][parent]>0):
      link_matrix[i][parent]=-1
    if(link_matrix[parent][i]>0):
      link_matrix[parent][i]=-1
      delete_node(i)

def find_leaf_node(root):
  isLeaf = True
  leafSum = 0
  for child in range(0, node_num):
    if(link_matrix[root][child]>0):
      isLeaf = False
      leafSum += find_leaf_node(child)
  if(isLeaf):
    leafSum = 1
  return leafSum

if(delete_node_index==root):
  print(0)
  sys.exit()
delete_node(delete_node_index)
print(find_leaf_node(root))