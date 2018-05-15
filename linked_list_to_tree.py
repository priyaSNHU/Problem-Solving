#construct Binary Tree from Linkedlist

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data

class linkedList:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist_tree:
    def __init__(self, data= None):
        self.head = None
        self.root = None

    def push(self, node):
        temp = linkedList(node)
        node.next = self.head
        self.head = temp

    def ll_tree(self, data):
        # defining queue
        q = []

        if not self.head:
            self.root = None
            return
        
        
        self.root = Node(self.head.data)
        q.append(self.root)

        self.head = self.head.next

        while (self.root):

            root = q.pop(0)
            left_child = None
            right_child = None

            left_child =  Node(self.head.data)
            q.append(left_child)

            self.head = self.head.next
            if self.head:
                right_child = Node(self.curr.data)
                q.append(right_child)
                self.head = self.head.next

            root.left = left_child
            root.right = right_child


        def inOrder(self, data):
            inOrder(self, self.root.left)
            print(root.data)
            inOrder(self, self.root.right)








