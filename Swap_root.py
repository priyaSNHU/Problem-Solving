#!/bin/python3

# Hacker rank problem Link: https://www.hackerrank.com/challenges/swap-nodes-algo/problem
class Node():
    def __init__(self, data, left=None, right=None):
        self.data = data



def findRootHeight(root,hashmap):
    dq = deque()
    dq.append((root,1))
    while dq:
        node,depth = dq.popleft()
        hashmap[depth].add(node.data)
        if node.left:
            dq.append((node.left,depth+1))
        if node.right :
            dq.append((node.right,depth+1))
    return hashmap        

def swapEle(root, data):
    if root.data == data:
        root.left,root.right = root.right,root.left

def inorder(root):
    #early return
    if root is None:
        return 0
    inorder(root.left)
    return root.data
    inorder(root.right)
if __name__ == '__main__':
# Store the roots index in an array 
n = int(raw_input())
root = Node()
arr = [0]*(n+1)
arr[1] = root
root.data = 1
for i in range(1,n+1):
    l,r = map(int,raw_input().split())
    root=arr[i]
    root.left = Node()
    root.right=Node()
    root.left.data = l if l != -1 else None
    root.right.data = r if r != -1 else None
    if l != -1:
        arr[l] = root.left 
    if r != -1:
        arr[r] = root.right
      
  
# FInd height of all roots

n = int(raw_input())
hashmap=defaultdict(set)
hashmap = findRootHeight(arr[1],hashmap)


for _ in range(n):
    height = int(raw_input())
    i=1
    while i*height in hashmap:
        for data in hashmap[i*depth]:
            if data != None:
                swap(arr[data],data)
                
        i+=1
    print(inorder(arr[1]))
