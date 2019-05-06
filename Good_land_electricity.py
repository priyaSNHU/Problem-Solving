# HACKER RANK PROBLEM LINK: https://www.hackerrank.com/challenges/pylons/problem
def trans_count(k, arr):
    # Complete this function
    curr = 0
    temp = 0
    no_of_chnges = 0
    while curr < len(arr):
        temp = curr + k -1
        if temp >= len(arr):
            temp = len(arr) - 1
        while (temp >= 0 and ((temp + k) > curr) and arr[temp] != 1):
            temp -= 1
        if temp < 0 or (temp + k) <= curr:
            return -1
        else:
            no_of_chnges += 1
        curr = temp + k
    return no_of_chnges

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = list(map(int, input().strip().split(' ')))
    print(trans_count(k, arr))

#input
# 6 2
# 0 1 1 1 1 0
