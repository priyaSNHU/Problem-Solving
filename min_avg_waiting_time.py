#!/bin/python3
# hacker rank problem link: https://www.hackerrank.com/challenges/minimum-average-waiting-time/problem



from heapq import heappush, heappop

import os
import sys

#
# Complete the minimumAverage function below.
#
def minimumAverage(customers,n):
    #
    # Write your code here.
    #
    customers.sort(reverse=True)

    pq = []
    waiting_time = 0
    current_time = 0

    while customers or pq:
        while customers and customers[-1][0] <= current_time:
            heappush(pq, customers.pop()[::-1])
        if pq:
            current_task = heappop(pq)
            current_time += current_task[0]
            waiting_time += current_time - current_task[1]
        else:
            heappush(pq, customers.pop()[::-1])
            current_time = pq[0][1]

    return (waiting_time // n)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    customers = []

    for _ in range(n):
        customers.append(list(map(int, input().rstrip().split())))

    result = minimumAverage(customers,n)

    fptr.write(str(result) + '\n')

    fptr.close()
