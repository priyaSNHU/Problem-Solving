#!/bin/python3

import sys

def minimumBribes(q):
    # Complete this function
    bribes = len(q)
    pos = {1,2}
    for i in range(n):
        pos |= {i+3}
        if q[i] in pos:
            if q[i]==min(pos):
                bribes -= 1
            if q[i]==max(pos):
                bribes += 1
            pos -= {q[i]}
        else:
            return 'Too chaotic'
            break
    else:
        return bribes
if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        q = list(map(int, input().strip().split(' ')))
        minimumBribes(q)
