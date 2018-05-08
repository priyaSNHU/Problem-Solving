# Hacker Rank Problem Link: https://www.hackerrank.com/challenges/is-binary-search-tree/problem



class node:
  def __init__(self, data, left = None, right = None):
      self.data = data
      

def check_binary_search_tree_(root):
    # 0<= data <= 10000
    # min_data = -1
    #max_data = 10001
    return CheckBST(root, -1 , 10001)

def CheckBST(root , min_data, max_data):
    if root is None:
        return True
    if root.data <= min_data or root.data >= max_data:
        return False

    return CheckBST(root.left, min_data , root.data) and CheckBST(root.right, root.data, max_data)
