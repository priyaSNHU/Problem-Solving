#Hacker Rank Problem Link: https://www.hackerrank.com/challenges/largest-rectangle/problem

#!/bin/python3

import os
import sys

# Complete the largestRectangle function below.
def largestRectangle(h):
    max_area = 0
    for i in range(len(h)):
        count = 0
        # check for continous buildings to the left
        for j in range(i, -1, -1):
            if h[j] >= h[i]:
                counnt += 1
            else:
                break
        #check for buildings to the right
        for k in range(i+1, len(h)):
            if h[k] >= h[i]:
                count += 1
            else:
                break
        #calculate the rectangle area
        area = h[i] * count
        if area > max_area:
            max_area = area
    return max_area

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
