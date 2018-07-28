# Problem Link: https://www.hackerrank.com/challenges/angry-children/problem


def minMax(n , k):
    if n < k:
        return
    if k < 1:
        return 
    min_diff = n[k-1] - n[0]
    
    for i in range((len(n) - k) +1 ):
        diff = n[ i + (k-1)] - n[i]
        if diff < min_diff:
            min_diff = diff
    return min_diff


n = [100,200,300,350,400,401,402]

k = 3

print(minMax(n,k))
        

