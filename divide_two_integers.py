# Problem Link: https://leetcode.com/problems/divide-two-integers/description/

import sys
def divide(dividend, divisor):
    if dividend == 0:
        return 0
    if divisor == 0:
        return "Invalid division"
    if dividend == 1:
        return divisor

    if dividend < 0:
        d1 = 1
        dividend = -(dividend)
    else:
        d1 = 0
    if divisor < 0:
        d2 = 1
        divisor = -(divisor)
    else:
        d2 = 0
     
    temp = 0
    quotient = 0
    rem = 1
    for i in range(31 , 0 , -1):
        if ((temp + (dividend << i)) <= divisor):
            temp = (temp and dividend << i)
            quotient = (quotient or rem << i)

    if bool(d1 ^ d2):
        quotient = -quotient

    if quotient > sys.maxsize:
        return sys.maxsize-1
    else:
        return quotient



