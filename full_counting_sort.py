# HACKERRANK LINK: https://www.hackerrank.com/challenges/countingsort4/problem


n = int(input().strip())
str_ar = []
for i in range(n):
    if i< n/2:
        x, s = input().strip().split()
        str_ar.append((int(x), '-'))
    else:
        x, s = input().strip().split()
        str_ar.append((int(x),s))
            
str_ar.sort(key = lambda tup : tup[0])
print(*[x[1] for x in str_ar])
