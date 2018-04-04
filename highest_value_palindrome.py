#!/bin/python3

import os
import sys


#
# Complete the highestValuePalindrome function below.
#
def highestValuePalindrome(s, n, k):
    #
    # Write your code here.
    #
    left=''
    right=''
    unmatched_chars=0
    for i in range(n//2):
        if s[i]!=s[n-1-i]:
            unmatched_chars+=1
    if k<unmatched_chars:
        return -1
    else:
        for i in range(n//2):
            left_str=s[i]
            right_str=s[n-1-i]
            if left_str == right_str:
                if left_str=='9' or k-2<unmatched_chars:
                    left+=left_str
                    right+=left_str
                    left+='9'
                    right+='9'
                    k-=2
            else:
                if k-1>=unmatched_chars and left_str!='9' and right_str!='9':
                    left+='9'
                    right+='9'
                    k-=2
                else:
                    if left_str > right_str:
                        left+=left_str
                        right+=left_str
                    else:
                        left+=right_str
                        right+=right_str
                    k-=1
                unmatched_chars-=1

    if n%2==1:
        if k>0:
            return left+'9'+right[::-1]
        else:
            return left+s[n//2]+right[::-1]
    else:  
        return left+right[::-1]



if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    s = input()

    result = str(highestValuePalindrome(s, n, k))

    f.write(result + '\n')

    f.close()
