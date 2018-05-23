# Hacker Rank Problem Link: https://www.hackerrank.com/challenges/truck-tour/problem

#!/bin/python3

import os
import sys

#
# Complete the truckTour function below.
#
def truckTour(petrolpumps, N):
    #
    # Write your code here.
    #
    pump = []
    dist = []
    start=0
    curr=0
    total=0
    for pair in petrolpumps:
        pump.append(pair[0])
        dist.append(pair[1])
    for i in range(N):
        total = total + pump[i] - dist[i]
        curr = curr + pump[i] - dist[i]
        if curr < 0:
            curr = 0
            start = i + 1
    if total < 0:
        return -1
    return start

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))
        
    
    result = truckTour(petrolpumps , n)

    fptr.write(str(result) + '\n')

    fptr.close()









## Another Approch using dequeue


from collections import deque

N = int(input())
petrolpumps = []
for i in range(N):
    pair = input().split()
    petrolpumps.append((int(pair[0]),int(pair[1])))

curr = 0
start = 0
total = 0
q = deque()
while len(q) < N:
    q.append(petrolpumps[curr % N])
    curr = curr + 1
    total = total + q[-1][0] - q[-1][1]
    while total < 0:
        (pump,dist) = q.popleft()
        total = total - pump + dist
        start=start+1
print(start)
