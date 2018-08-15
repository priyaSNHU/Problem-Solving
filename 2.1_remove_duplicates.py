# Problem: Write code to remove duplicates from an unsorted linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_duplicates(head):
    if not head:
        return

    current = head
    successor = current
    while current is not None:
        while successor.next is not None:
            if successor.next.data == current.data:
                successor.next = successor.next
            else:
                successor = successor.next

        current = current.next

    return head


def delete_duplicates(head):
    list_nodes = set([head.data])
    curr = head
    succ = curr.next
    while curr.next:
        if succ.data in list_nodes:
            curr.next = succ.next
        else:
            curr = succ
            list_nodes.add(curr.data)
    return list_nodes



