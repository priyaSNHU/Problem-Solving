# Problem: Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_middle_node(head , n):
    current = head
    if current == n:
        return
    while current.next:
        if current.next == n:
            if current.next.next:
                current.next = current.next.next
                return
            else:
                print('Invalid node, Cannot delete last node')
                return
        current = current.nextnode
    
