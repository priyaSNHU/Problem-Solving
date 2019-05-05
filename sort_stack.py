class stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.stack[-1]
    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.stack.pop()
    def size(self):
        return len(self.stack)
    def isEmpty(self):
        return self.size() == 0


# Sort stack using iterative method using addtional stack
def sort_ascending(stack1):
    stack2 = stack()
    while not stack1.isEmpty():
        temp = stack1.pop()
        while (not stack2.isEmpty() and stack2.peek() > temp):
            stack1.push(stack2.pop())
        stack2.push(temp)
    return stack2

# sort stack using recursion method
def sort_stack_rec(stack1):
    if not stack1.isEmpty():
        temp = stack1.pop()
        sort_stack_rec(stack1)
        sort_and_push(stack1 , temp)

def sort_and_push(stack1, temp):
    if stack1.isEmpty() or temp > stack1.peek():
        stack1.push(temp)
    else:
        temp = stack1.pop()
        sort_and_push(stack1, temp)
        stack1.push(temp)
    
stack1 = stack()
stack1.push(34)
stack1.push(78)
stack1.push(82)
stack1.push(15)

print("\n sorting stack using another stack method")
stack2 = sort_ascending(stack1)
while not stack2.isEmpty():
    print(stack2.pop())
print("\n sorting stack using recursion method")
sort_stack_rec(stack1)
print(stack1)


























    
