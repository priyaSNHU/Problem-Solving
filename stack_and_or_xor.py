#hacker Rank problem link: https://www.hackerrank.com/challenges/and-xor-or/problem

#!/bin/python3

import os
import sys


class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def peek(self):
        if self.isEmpty():
            return None
        return self.stack[-1]
    def pop(self):
        if self.isEmpty():
            return None
        return self.stack.pop()
    def size(self):
        return len(self.stack)
    def isEmpty(self):
        return self.size() == 0

def andXorOr(a):
    
    max_value = a[0]^a[1]
    stack = Stack()
    for i in a:
        while not stack.isEmpty():
            top = stack.peek() 
            stack_oper = i^top  
            if stack_oper > max_value:  # yield
                max_value = stack_oper
            if i < top:
                stack.pop()
            else:
                break
        stack.push(i)
    return max_value

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = list(map(int, input().rstrip().split()))

    result = andXorOr(a)

    fptr.write(str(result) + '\n')

    fptr.close()
