# problem: https://www.hackerrank.com/challenges/down-to-zero-ii/problem

from math import sqrt, floor


def downToZero(n):
    dz_list = [n]
    moves = 0
    visited = set()
    
    while dz_list:
        if 0 in dz_list:
            return moves
        operation = []
        for val in dz_list:
            operation += [max(i, val // i ) for i in range(2, floor(sqrt(val))+1) if val%i == 0]
            operation.append(val - 1)
        nq = set(operation)
        dz_list = list(nq - visited)
        visited |= nq
        moves += 1
            
if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        n = int(input())

        print(downToZero(n))
    
