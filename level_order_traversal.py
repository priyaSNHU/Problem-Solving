#print level-order-traversal
class Node:
    def __init__(self, data):
        self.data = data
        self.left= None
        self.right = None
        
def level_traversal(root):
    traversal = []
    if root is None:
        return traversal
    level_order = [root]
    while len(level_order) > 0:
        curr_level = []
        next_level = []
        for curr in level_order:
            curr_level.append(curr.data)
            if curr.left is not None:
                next_level.append(curr.left)
            if curr.right is not None:
                next_level.append(curr.right)
        traversal.append(curr_level)
        level_order = next_level
    return traversal

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
print(level_traversal(root))












        
