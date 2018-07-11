#Hacker Rank Problem: https://www.hackerrank.com/challenges/non-divisible-subset/problem

def nonDivisibleSubset(k , arr):
    if k <= 0:
        return None
    if not s:
        return None
    
    num=[0]*k
    for i in arr:
        num[i % k]+=1
    count = min(1, num[0])
    for j in range(1, (k+1)//2):
        count += max(num[j],num[k-j])
    if k % 2 == 0 and num[(k//2) + 1]>0:
        count = count+1 
    print(count)


k = -1
s = [1, 7, 2, 4]

nonDivisibleSubset(k,s)

k = 0
s = [1, 7, 2, 4]

nonDivisibleSubset(k,s)

k = 5
s = [1, 7, 2, 4]

nonDivisibleSubset(k,s)

k = 2
s = []

nonDivisibleSubset(k,s)





                
