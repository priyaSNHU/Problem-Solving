#!/bin/python3

import os
import sys

#
# Complete the gamingArray function below.
#
def gamingArray(arr):
    #
    # Write your code here.
    #
    moves = 0
    max_arr = 0
    n = len(arr)
    # go through the list
    for i in range(n):
        value = arr[i]
        if value > max_marr:
            max_arr = value
            moves+=1
    #check who wins the game
    if moves%2==0:
        name = 'ANDY'
    else:
        name=  'BOB'
    return name

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        arr_count = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = gamingArray(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
