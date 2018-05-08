class Node:
    def __init(self, root, left = None, right = None):
        self.data = root

# Python BFS
def levelOrder(root):
    # Early return
    if root is None:
        return
    # declare queue to keep track of tree elements
    queue = []

    queue.append(root)

    while len(queue):
        print(queue[0].data)
        root = queue.pop(0)

        if root.left:
            queue.append(root.left)

        if root.right:
            queue.append(root.right)
    
    
#python BFS
# In order traversal

def inOrder(root):
    #early return
    if root is None:
        return
    else:
        inOrder(root.left)
        print(root.data)
        inOrder(root.right)

# PostOrder traversal

def postOrder(root):
    #early return
    if root is None:
        return
    else:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data)


# Pre order traversal

def preOrder(root):
    #early return
    if root is None:
        return
    else:
        print(root.data)
        preOrder(root.left)
        preOrder(root.right)


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
levelOrder(root)
inOrder(root)
postOrder(root)
preOrder(root)



























