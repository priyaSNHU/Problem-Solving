# HACKERRANK PROBLEM LINK: https://www.hackerrank.com/challenges/lilys-homework/problem

#!/bin/python3

import sys

def lilysHomework(arr):
    # Complete this function
    mapping_list = {}
    for i in range(len(arr)):
        mapping_list[arr[i]] = i
    sort_arr = sorted(arr)
    no_swaps = 0
    for i in range(len(arr)):
        if arr[i] != sort_arr[i]:
            no_swaps += 1
            
            swap_ind = mapping_list[sort_arr[i]]
            mapping_list[arr[i]] = mapping_list[sort_arr[i]]
            arr[i], arr[swap_ind] = sort_arr[i], arr[i]
    return no_swaps
    
    

if __name__ == "__main__":
    input()
    arr = [int(i) for i in input().split(' ')]
    result = lilysHomework(list(arr))
    desc_result = lilysHomework(list(reversed(arr)))
    print( min(result, desc_result))
