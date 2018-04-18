# HAcker Rank Problem: https://www.hackerrank.com/challenges/the-strange-function/problem
#!/bin/python3

import sys

def find_gcd(x, y): 
    while(y):
        x, y = y, x % y
     
    return x

def f(a,l,r):
    gcd_list = a[l]
    for i in a[l+1: r+1]:
        gcd_list = find_gcd(gcd_list , i)
    return gcd_list *(sum(a[l:r+1]) - max(a[l:r+1]))
    

def maximumValue(a):
    # Return the maximum value of f among all subsegments [l..r].
    if len(a) == 0:
        return 0
    result = 0
    for l in range(len(a)):
        for r in range(l, len(a)):
            result = max(result , f(a,l,r))
    return result
            

if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    print(maximumValue(a))
    
