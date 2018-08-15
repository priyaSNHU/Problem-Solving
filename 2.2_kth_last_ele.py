#Problem: Implement an algorithm to find the kth to last element of a singly linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def find_kth_last_recur(head , k):
    if not head:
        return
    if k == find_kth_last_recur(head.next , k) + 1:
        return head.data
    return find_kth_last_recur(head.next , k) + 1


def find_kth_last_iter(head, k):
    if not head:
        return

    curr = head
    while k > 0:
        curr = curr.next
        k -= 1

    succ = head
    while curr:
        curr = curr.next
        succ = succ.next

    return succ.data
    
    
