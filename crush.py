#Hackerrank Problem: https://www.hackerrank.com/challenges/crush/problem
#Time COmplexity: O(n)
#space complexity : O(1)


def array_manipulation(n , m):
    nums_lis= [0] * (n+1)
    max_value = 0
    temp_val = 0
    for _ in range(m):
        a,b,k = (map(int, input().rstrip().split()))
        nums_lis[a - 1] += k
        if b < len(nums_lis):
            nums_lis[b] -= k
    
    for num in nums_lis:
        temp_val = temp_val+num
        if max_value < temp_val:
            max_value = temp_val
    return max_value
print("Enter the length of list: ")
n = int(input())
print("enter the number of queries: ")
m = int(input())

print(array_manipulation(n,m))
