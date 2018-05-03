#!/bin/python3
# Hacker Rank Problem: https://www.hackerrank.com/challenges/poisonous-plants/problem
# time Complexity: O(n)


def poisonousPlants(plants):
    # Complete this function
    stack = []
    maxDays = 0

    for i in range(0, len(plants)):
        plant = plants[i]
        mdays = 0
        while len(stack) != 0 and stack[len(stack) - 1][0] >= plant:
            other_plant = stack.pop()
            mdays = max(other_plant[1], mdays)
        if len(stack) != 0 :
            days = mdays + 1
        else :
            days = 0
        stack.append( (plant, days) )
        maxDays = max(days, maxDays)
    
    return maxDays

if __name__ == "__main__":
    n = int(input().strip())
    plants = list(map(int, input().strip().split(' ')))
    result = poisonousPlants(plants)
    print(result)
