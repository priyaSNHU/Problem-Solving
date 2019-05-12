#!/bin/python3

import sys
class division:
    def stoneDivision(self, n, s):
        # Complete this function
        self.s = s
        self.dict = dict()
        return self.helper(n)
    
    def helper(self, n):
        if n in self.dict:
            return self.dict[n]
        temp_moves = 0
        for i in self.s:
            if i < n and n % i == 0:
                temp_moves = max(1+ (n//i)* self.helper(i), temp_moves)
            if i >= n:
                break
        self.dict[n] = temp_moves
        return self.dict[n]
    
    

if __name__ == "__main__":
    q = int(input().strip())
    d = division()
    for a0 in range(q):
        n, m = input().strip().split(' ')
        n, m = [int(n), int(m)]
        s = list(map(int, input().strip().split(' ')))
        s = sorted(s)
        result = d.stoneDivision(n, s)
        print(result)
