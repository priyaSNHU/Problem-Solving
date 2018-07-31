## Problem Link: https://www.hackerrank.com/challenges/minimum-swaps-2/problem

def minSwaps(arr):
    if len(arr) == 1:
        return 0

    count=0

    for i in range(len(arr)):
        if arr[i] != i+1:
            temp = arr.index(min(arr[ i + 1 : len(arr)]))
            arr[i], arr[temp]= arr[temp],arr[i]
            count+=1
        else:
            continue

    return count


