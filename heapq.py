# Hacker rank Problem: https://www.hackerrank.com/challenges/qheap1/problem
#Time COmplexity: O(n)
# Space COmplexity: O(n)
from heapq import heappush, heappop

add_heap = []
del_heap = []
q = int(input().strip())
for i in range(q):
    lst = list(map(int, input().strip().split(' ')))
    # 1: add element to heap
    if lst[0] == 1:
        heappush(add_heap, lst[1])
    #2: delete element from heap
    elif lst[0] == 2:
        if add_heap[0] == lst[1]:
            heappop(add_heap)
        else:
            heappush(del_heap, lst[1])
    #3: minimum of the heap
    elif lst[0] == 3:
        flag = bool(del_heap)
        while flag:
            if del_heap[0] == add_heap[0]:
                heappop(del_heap)
                heappop(add_heap)
                flag = bool(del_heap)
            else:
                flag = False

        print (valheap[0])
