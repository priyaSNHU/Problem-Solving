#!/bin/python3

import os
import sys

#
# Complete the bonetrousle function below.
#

def bonetrousle(n, k, b):
    #
    # Write your code here.
    min_sum = b*(b+1)//2
    max_sum = b*((k-b+1)+k)//2 
    if n == min_sum:
        boxes_list = [box for box in range(1, b+1)]
    elif n == max_sum:
        boxes_list = [box for box in range(k-b+1,k+1)]
    elif min_sum < n > max_sum:
        boxes_list = [box for box in range(1, b+1)]
        temp = min_sum
        for i in range(len(boxes_list)-1,0,-1):
            temp -= boxes_list[i]
            diff = n - temp
            boxes_list[i] = min(k, diff)
            temp += boxes_list[i]
            k = boxes_list[i] - 1
            if temp == n:
                break
    else:
        boxes_list = [-1]
    return boxes_list
            
    

if __name__ == '__main__':
    

    t = int(input())

    for t_itr in range(t):
        nkb = input().split()

        n = int(nkb[0])

        k = int(nkb[1])

        b = int(nkb[2])

        result = bonetrousle(n, k, b)

        print(result)
