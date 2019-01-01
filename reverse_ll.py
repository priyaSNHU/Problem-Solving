# Reverse Linkedlist pair wise

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        curr = Node(data)
        curr.next = self.head
        self.head = curr

    def printLL(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    # reverse linkedlist pairwise based on interval
    def reverse_pw(self, head, I):
        curr = head
        prev = None
        temp = None
        interval = 0
        while curr is not None and interval < I:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            interval += 1

        if temp is not None:
            head.next = self.reverse_pw(temp , I)

        return prev

    # reverse pairwise linkedlist using recursion
    def reverse_recurll(self, head):
        if head is None or head.next is None:
            return head
        
        temp = head.next.next
        new_head = head.next
        head.next.next = head
        head.next = self.reverse_recurll(temp)

        return new_head

    #reverse pairwise linkedlist using iterative method

    def reverse_iterll(self):
        head = self.head
        if head is None:
            return
        while (head is not None and head.next is not None):
            temp = head
            head = head.next
            head.next = temp
            head = head.next.next
#TestCases
ll = LinkedList() 
ll.push(9) 
ll.push(8) 
ll.push(7) 
ll.push(6) 
ll.push(5) 
ll.push(4) 
ll.push(3) 
ll.push(2) 
ll.push(1) 
ll.head = ll.reverse_pw(ll.head, 2)  
print("\nReversed Linked list based on intervals")
ll.printLL()

ll = LinkedList()
ll.push('d')
ll.push('c')
ll.push('b') 
ll.push('a') 
ll.head = ll.reverse_recurll(ll.head)  
print("\nReversed Linked list using recursion")
ll.printLL()
























        
            
