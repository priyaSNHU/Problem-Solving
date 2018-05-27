# Hacker Rank Problem Link: https://www.hackerrank.com/challenges/dynamic-array/problem

#!/bin/python3

import os
import sys

#
# Complete the dynamicArray function below.
#
def dynamicArray(n, queries):
    #
    # Write your code here.
    #
    lastAns = 0
    seqList = [[]]* n
    for query in queries:
        if query[0] == 1:
            seqIndex  = (query[1] ^ lastAns) % n
            seqList[seqIndex] = seqList[seqIndex] + [query[2]]
        elif query[0] == 2:
            seqIndex = (query[1] ^ lastAns) % n
            value = query[2] % len(seqList[seqIndex])
            lastAns = seqList[seqIndex][value]
            print(lastAns)

if __name__ == '__main__':
    
    nq = input().split()

    n = int(nq[0])

    q = int(nq[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))
    
    result = dynamicArray(n, queries)

