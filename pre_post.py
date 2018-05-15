# construct tree from given inorder and postorder
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
def buildTree(inOrder, preOrder):
    return buildtree_helper(0, len(inorder))

def buildtree_helper(start, end):
    if start < end:
        root = Node(self.postorder.pop())
        index = inorder.index(root.data)
        root.right = buildtree_helper(index + 1, end)
        root.left = buildtree_helper(start, index)
        return root
