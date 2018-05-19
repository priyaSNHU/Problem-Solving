#!/bin/python3

import os
import sys

#check if number is prime or not
def isPrime(num):
    if num == 0 or num == 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    else:
        return True


# find the ith prime number
def nextPrime(prime):           
    nextNum = prime + 1
    while not isPrime(nextNum):
        nextNum += 1
    return nextNum


#
# Complete the waiter function below.
#
def waiter(number, q):
    #
    # Write your code here.
    #
    # plate ranking queue
    plate_rank = []                         
    prime = 2
    for i in range(q):
        # Divide whole list into even_plates and odd_plates
        odd_plates = []                       
        even_plates = []
        while number:
            num = number.pop()              
            if num % prime == 0:
                even_plates.append(num)     
            else:
                odd_plates.append(num)
                
        number = odd_plates                     
        for i in range(len(even_plates)):
            plate_rank.append(even_plates.pop()) 
            
        prime = nextPrime(prime)              
        
    # to append last values into plate rank  
    for i in range(len(number)):
        plate_rank.append(number.pop())
             
    return plate_rank

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().split()

    n = int(nq[0])

    q = int(nq[1])

    number = list(map(int, input().rstrip().split()))

    waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
