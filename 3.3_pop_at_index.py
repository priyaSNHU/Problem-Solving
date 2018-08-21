# Problem : Imagine a stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would literally start a new stack when the previous stack exceeds some threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack (that is, pop() should return the same values as it would if there were just a single stack).
# FOLLOW UP: Implement a function popAt(index) which performs a pop operation on a specific sub-stack

class stack_of_plates:
    # Lets Assume max_capacityof each stack is 10
    def __init__(self):
        self.stacks = []
        self.last = None

    def push(self, value):
        if self.stacks[self.last].size() >= max_capacity:
            self.stacks.append(stack())
            self.last = self.last + 1
        self.stacks[self.last].push(value)

    def pop(self):
        if self.stacks[self.last].size() <= 0:
            if len(self.stacks) <= 1:
                return
            del self.stacks[self.last]
            self.last = self.last - 1
        return self.stacks[self.last].pop()

    def popAt(self, index):
        if (index < 0) or (index > self.last):
            return False
        temp = self.stacks[index].pop()
        if self.stacks[index].size() <= 0:
            del self.stacks[index]
            self.last = self.last - 1
        return temp

