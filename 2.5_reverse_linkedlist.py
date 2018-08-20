#Problem: Writea function that adds the two numbers and returns the sum as a linked list. The digits are stored in reverse order

class Node():
    def __init__(self , data):
        self.data = data
        self.next = None


def addTwoLists(self, first_ll, second_ll):
    prev , temp = None
    carry = 0
    while(first_ll is not None or second_ll is not None):
        fdata = 0 if first_ll is None else first_ll.data
        sdata = 0 if second_ll is None else second_ll.data
        Sum = carry + fdata + sdata
        carry = 1 if Sum >= 10 else 0
        Sum = Sum if Sum < 10 else Sum % 10
        temp = Node(Sum)
        if self.head is None:
            self.head = temp
        else :
            prev.next = temp 
        prev = temp
        if first_ll is not None:
            first_ll = first_ll.next
        if second_ll is not None:
            second_ll = second_ll.next
    if carry > 0:
        temp.next = Node(carry)
 
    
