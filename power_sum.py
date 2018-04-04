# HACKER RANK PROBLEM LINK: https://www.hackerrank.com/challenges/the-power-sum/problem

import math

def powerSum(integer, power, carry_num):
    # Complete this function
    int_diff = int(math.pow(carry_num,power))
    if int_diff > integer:
        return 0
    elif int_diff == integer:
        return 1
    else:
        return powerSum(integer, power, carry_num+1) + powerSum(integer - int_diff , power, carry_num+1)
