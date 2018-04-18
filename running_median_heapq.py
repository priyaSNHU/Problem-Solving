#HACKER RANK PROBLEM: https://www.hackerrank.com/challenges/find-the-running-median/problem
#!/bin/python3


from heapq import *

N = int(input().strip())

min_heap = []    
max_heap = []    
median = 0
for i in range(N):
    n = int(input().strip())
    if n > median:
        heappush(max_heap , n)
    else:
        heappush(min_heap , -n)

    if len(min_heap) > len(max_heap) + 1:
        heappush(max_heap , -heappop(min_heap))
    if len(max_heap) > len(min_heap) + 1:
        heappush(min_heap , -heappop(max_heap))

    if len(min_heap) == len(max_heap):
        m1 = -heappop(min_heap)
        heappush(min_heap, -m1)
        m2 = heappop(max_heap)
        heappush(max_heap, m2)

        median = (m1 + m2) / 2
    elif len(min_heap) == len(max_heap) + 1:
        m = -heappop(min_heap)
        heappush(min_heap, -m)
        median = m
                           
    else:
        m = heappop(max_heap)
        heappush(max_heap, m)
        median = m
    
    print(median)
    
        

