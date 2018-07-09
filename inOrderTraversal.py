## Inorder traversal with out recursion and without using stacks.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inOrderTraversalIterative(root):
    if root is None:
        return None
    
    curr = root

    while curr:
        if curr.left is None:
            print(curr.data)
            curr = curr.right
        else:
            prev = curr.left
            while (prev.right and prev.right != curr):
                prev = prev.right


            if not prev.right:
                prev.right = curr
                curr = curr.left

            else:
                prev.right = None
                print(curr.data)
                curr = curr.right

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
inOrderTraversalIterative(root)





                
