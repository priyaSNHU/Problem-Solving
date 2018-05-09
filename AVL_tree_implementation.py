class Node:
    def __init__(self, data, left= None, right= None):
        self.data = data

class AVL_tree:
    def __init__(self):
        self.root = None
        self.height = -1
        self.balance = 0
    #get height of tree
    def getHeight(self):
        if self.root:
            return self.root.height
        else:
            return 0
    def getBalance(self):
        if self.root:
            return self.getHeight(root.left)- self.getHeight(root.right)

    def minRoot(self, root):
        if not root or not root.left:
            return root
        return self.minRoot(root.left)
    #insert ele
    def insertEle(self, data):
        avl_tree = self.root)
        new_root = Node(data)

        if not avl_tree:
            self.root = new_root
            self.root.left = AVL_tree()
            self.root.right = AVL_tree()
        elif data < root.data:
            self.root.left.insertEle(data)
        elif data > root.data:
            self.root.right.insertEle(data)

        self.reBalance()
    #update balace
    def balanceUpdate(self, recursivee=True):
        if self.root:
            if recursive:
                if not self.root.left:
                    self.root.left.balanceUpdate()
                if self.node.right is not None:
                    self.root.right.balanceUpdate()

            self.balance = self.root.left.height - self.root.right.height
        else:
            self.balance = 0
    #update Height
    def heightUpdate(self, recursive=True):
        if not self.root is None:
            if recursive:
                if not self.root.left:
                    self.root.left.heightUpdate()
                if not self.root.right :
                    self.node.right.heightUpdate()

            self.height = max(self.root.left.height,
                              self.root.right.height) + 1
        else:
            self.height = -1

    def reBalance(self):
        self.heightUpdate(False)
        self.balanceUpdate(False)
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.root.left.balance < 0:
                    self.root.left.rotate_left()
                    self.heightUpdate()
                    self.balanceUpdate()
                self.rightRotate()
                self.heightUpdate()
                self.balanceUpdate()

            if self.balance < -1:
                if self.root.right.balance > 0:
                    self.root.right.rightRotate()
                    self.heightUpdate()
                    self.balanceUpdate()
                self.leftRotate()
                self.heightUpdate()
                self.balanceUpdate()

    # rotate right
    def rightRotate(self):
        new_root = self.root
        new_left_child = self.root.left.root
        new_right_child = new_left_child.right.root

        self.root = new_left_child
        new_left_child.right.root = new_root
        new_root.left.root = new_right_child

        
    # rotate left
    def leftRotate(self):
        new_root = self.root
        new_right_child = self.root.right.root
        new_left_child = new_right_child.left.root

        self.root = new_right_child
        new_right_child.left.root = new_root
        new_root.right.root = new_left_child


    def balanceCheck(self):
        if self.root is None:
            return True

        self.heightUpdate()
        self.balanceUpdate()
        return ((abs(
            self.balance) < 2) and self.root.left.balanceCheck() and
                self.root.right.balanceCheck())


    def delete(self, root, data):
        if not self.root:
            return self.root
        elif data < self.root.data:
            self.root.left = self.delete(self.root.left, data)
        elif data > self.root.data:
            self.root.right = self.delete(self.root.right, data)
        else:
            if self.root.left is None:
                temp = self.root.right
                self.root = None
                return temp
            elif self.root.right is None:
                temp = self.root.left
                self.root = None
                return temp
            temp = self.minRoot(self.root.right)
            self.root.data = temp.data
            self.root.right = self.delete(self.root.right,
                                      temp.data)
        # tree has only one node
        if self.root is None:
            return self.root
       # Update the height of the 
        self.root.height = 1 + max(self.getHeight(self.root.left),
                            self.getHeight(self.root.right))
        self.balance = self.getBalance(self.root) 
        # Left Left
        if self.balance > 1 and self.getBalance(self.root.left) >= 0:
            return self.rightRotate(self.root)
        # Right Right
        if self.balance < -1 and self.getBalance(self.root.right) <= 0:
            return self.leftRotate(self.root)
        # Left Right
        if self.balance > 1 and self.getBalance(self.root.left) < 0:
            self.root.left = self.leftRotate(self.root.left)
            return self.rightRotate(self.root)
        # Right Left
        if self.balance < -1 and self.getBalance(self.root.right) > 0:
            self.root.right = self.rightRotate(self.root.right)
            return self.leftRotate(self.root)
        return self.root

    def print_tree(self, root=None, level=0):
        if not root:
            root = self.root

        if root.right.node:
            self.print_tree(root.right.root, level + 1)
            print(('\t' * level), (' / '))
        print(('\t' * level), root.data)

        if root.left.root:
            print(('\t' * level), (' \\ '))
            self.print_tree(root.left.root, level + 1)

a = AVL_tree()
    tree_list = [7, 5, 2, 6, 3, 4, 1, 8, 9, 0]
    for i in tree_list: 
        a.insertEle(i)
         
    a.print_tree()
    
    a.delete(3)
    a.delete(4)
    a.print_tree()
    
    






















        
