#function to mirror the given binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left= None
        self.right = None
        
def mirror_tree(root):
    if root is None:
        return None
    mirror_tree(root.left)
    mirror_tree(root.right)
    root.left , root.right = root.right , root.left
    return root
    

def list_tree(a):
    if len(a) == 0:
        return None
    if len(a) == 1:
        root = Node(a[0])
        return root
    mid_point= int(len(a)/2)
    root = Node(a[mid_point])
    root.left = list_tree(a[0:mid_point])
    root.right = list_tree(a[(mid_point+1) :])
    return root



numbers =sorted([int(x) for x in input().split()])
root = list_tree(numbers)
print(mirror_tree(root))












        
