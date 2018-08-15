# Problems: Given a linked list and a value x, partition it such that all nodes less than x come first, then all nodes with value equal to x and finally nodes with value greater than or equal to x. The original relative order of the nodes in each of the three partitions should be preserved.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def partition(head, x_val):
    curr = head
    temp = head
    while curr:
        if curr.data < x_val:
            temp.data , curr.data = curr.data , temp.data

            curr = curr.next
            temp = temp.next
        else:
            curr = curr.next

    return curr


            
        
            
    
