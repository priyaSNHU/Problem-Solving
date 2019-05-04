class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

        
    def add_linkedlists(self, ll1, ll2):
        prev = None
        curr = None
        carry_sum = 0

        while ll1 is not None or ll2 is not None:
            if ll1 is None:
                ll1_data = 0
            else:
                ll1_data = ll1.data

            if ll2 is None:
                ll2_data = 0
            else:
                ll2_data = ll2.data

            ll_sum = carry_sum + ll1_data + ll2_data
            # if the sum is greater than 10 carry out the 1 to next adding data
            if ll_sum >= 10:
                carry_sum = 1
            else:
                carry_sum = 0
            #check if last added digits are greater than 10
            if ll_sum < 10:
                ll_sum = ll_sum
            else:
                ll_sum = ll_sum%10

            curr = Node(ll_sum)
            # continue with other elements in the linked list
            if self.head is None:
                self.head = curr
            else:
                prev.next = curr

            prev = curr

        
            if ll1 is not None:
                ll1 = ll1.next
            if ll2 is not None:
                ll2 = ll2.next

        if carry_sum > 0:
            curr.next = Node(carry_sum)

    def print_ll(self):
        curr = self.head
        while(curr):
            print (curr.data)
            curr = curr.next
    
        
        
ll1 = Linkedlist()
ll1.push(6)
print("linkedlist 1: ")
ll1.print_ll()

ll2 = Linkedlist()
ll2.push(4)
print("linkedlist2: ")
ll2.print_ll()

print("sum of two linkedlists is: ")

ll = Linkedlist()

ll.add_linkedlists(ll1.head, ll2.head)
ll.print_ll()












        
        
