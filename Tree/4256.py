import sys
get_input = lambda : sys.stdin.readline()

case_num = int(get_input())

def print_post_order(pre_list, in_list):
  
  if(not(pre_list)):
    return
  root = pre_list[0]

  root_index_on_inorder = find_root_index(root, in_list)
  
  #slice both lists
  left_inorder = in_list[0:root_index_on_inorder]
  right_inorder = in_list[root_index_on_inorder+1:len(in_list)]
  left_preorder = pre_list[1:root_index_on_inorder+1]
  right_preorder = pre_list[root_index_on_inorder+1:len(pre_list)]

  #Recursive Function
  print_post_order(left_preorder, left_inorder)
  print_post_order(right_preorder, right_inorder)

  #print root
  print(root, end=" ")

def find_root_index(root, given_list):
  for index in range(len(given_list)):
    if(root == given_list[index]):
      return index

while case_num :
  #Input
  node_num = int(get_input())
  pre_order_list = list(map(int, get_input().split()))
  in_order_list = list(map(int, get_input().split()))

  print_post_order(pre_order_list, in_order_list)
  print("")
  case_num -= 1