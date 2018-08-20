#Problem: Given a circular linked list, implement an algorithm which returns the node at the beginning of the loop

class Node:
    def __init__(self, data):
        self. data = data
        self.next = None


def circular_ll(head):
    if head is None:
        return
    curr, prev = head
    while curr and curr.next:
        curr = curr.next.next
        prev = prev.next
        if curr == prev:
            break
    if curr is None or curr.next is None:
        return
    prev = head
    while curr != prev:
        curr = curr.next
        prev = prev.next
    return curr





