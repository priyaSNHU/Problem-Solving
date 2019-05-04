#HackerRank Problem Link: https://www.hackerrank.com/challenges/pairs/problem
#!/bin/python3

import sys

# idea is to use dict and iterate to check if num + target in values stored in dict
# time complexity : O(n)
def pairs(target, arr):
    new_arr = dict()
    count = 0
    for num in arr:
        new_arr[num] = num
    for num in arr:
        temp = num + target
        if temp in new_arr:
            count += 1
    return count
     
# Set performs similar to dictionary but complete the process of check in one iteration process.
#time COmplexity: O(n)
def pairs(target, arr):
    # Complete this function
    new_arr = set()
    count = 0
    for num in arr:
        if num + target in new_arr:
            count += 1
        if num - target in new_arr:
            count += 1
        new_arr.add(num)
    return count
        

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = list(map(int, input().strip().split(' ')))
    result = pairs(k, arr)
    print(result)
