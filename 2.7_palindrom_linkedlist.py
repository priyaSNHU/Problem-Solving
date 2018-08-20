# Problem: Implement a function to check if given linkedlist is palindrome

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def palindrome_linkedlist(head):
    temp = None
    curr = head
    while curr and curr.next:
        curr = curr.next.next
        head.next , temp , head = temp , head, head.next

    prev = head.next if curr else head

    is_palindrome = True
    while temp:
        is_palindrom = is_palindrome and temp.data == prev.data
        temp.next , head, temp = head, temp , temp.next

        prev = prev.next
    return is_palindrome


    
