# Hacker Rank Problem Link: https://www.hackerrank.com/challenges/dynamic-array/problem

def seqIndex(x , lastAns , n):
    return (x ^ lastAns) % n


def dynamicArray(n, queries):
   
    lastAns = 0
    seqList = [[]]* n
    value = 0
    
    for query in queries:
        if query[0] == 1:
            seqList[seqIndex(query[1], lastAns , n)] = seqList[seqIndex(query[1], lastAns , n)] + [query[2]]
        elif query[0] == 2:
            try:
                value = query[2] % len(seqList[seqIndex(query[1], lastAns , n)])
            except ZeroDivisionError:
                 print ("You can't divide by zero")
                 break
            lastAns = seqList[seqIndex(query[1], lastAns , n)][value]
            print(lastAns)
        else:
            return None

    
print("Enter length of seqList: ")
n = int(input())
print("Enter number of quries: ")
q = int(input())

queries = []

for _ in range(q):
    queries.append(list(map(int, input().strip().split())))

dynamicArray(n, queries)


