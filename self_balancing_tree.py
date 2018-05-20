# Hacker rank problem link: https://www.hackerrank.com/challenges/self-balancing-tree


class Node:
    def __init__(self,data , left=None, right=None):
        self.data = data
        self.height = 0


def height(root):
    if root:
        return 1 + max(height(root.left), height(root.right))
    return -1

def updateHeight(root):
    if root:
        return 1 + max(height(root.left), height(root.right))
    return -1 

def rotateLeft(root):
    curr = root.right
    prev = root.left

    root.right = prev
    curr.left = root

    updateHeight(curr)
    updateHeight(root)

    return curr

def rotateRight(root):
    curr = root.left

    root.left = curr.right
    curr.right = temp

    updateHeight(curr)
    updateHeight(root)

    return curr

def insert(root, data):
    if not root:
        root = Node()
        root.data = data
        root.height = 0
        root.left = None
        root.right = None
        return root

    if root.data < data:
        root.right = insert(root.right , data)

    if root.data > data:
        root.left = insert(root.left , data)


    updateHeight(root)

    balance_factor = height(root.left) - height(root.right)


    if balance_factor > 1:
        if height(root.left.left) >= height(root.left.right):
            root = rotateRight(root)
        else:
            root.left = rotateLeft(root.left)
            root = rotateRight(root)

    elif balance_factor < -1:
        if height(root.right.right) >= height(root.right.left):
            root.leftRotation(root)
        else:
            root.right = rotateRight(root.right)
            root = rotateLeft(root)
    else:
        root.height = updateHeight(root)

    return root





















            
























    
        
