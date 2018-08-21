# Problem: Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

class stack:
    def __init__(self):
        self.min_ele = None
        self.stack = []

    def push(self,data):
        if self.stack.is_empty():
            min_ele = data
            self.stack.push(data)
        if data < min_ele:
            self.stack.push(2* data - min_ele)
            min_ele = data
        else:
            self.stack.push(data)
    def pop(self):
        if self.stack.is_empty():
            return
        temp = self.stack.pop()

        if temp < min_ele:
            print(min_ele)
            min_ele = 2*min_ele - temp
        else:
            print(temp)

    def get_min(self):
        if self.stack.is_empty():
            return
        else:
            print(min_ele)

