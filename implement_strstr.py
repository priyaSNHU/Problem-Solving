
#LeetCode: https://leetcode.com/problems/implement-strstr/ [simple]

# Return start index of substr else return -1
def implement_str1(a,b):
    return a.find(b)

# Alternate Approach
def implement_str2(a,b):
    if len(b) > len(a):
        return -1
    if not a or not b:
        return 0
    n = len(b)
    for i in range(len(a)):
        if a[i] == b[0]:
            if a[i : i + n] == b:
                return i

    return -1


#Test Cases
A = ''
B = ''
print("function with find method: {} ".format(implement_str1(A,B)))
print("Function with iterating: {}".format(implement_str2(A,B)))


A = 'a'
B = 'Aa'
print("function with find method: {} ".format(implement_str1(A,B)))
print("Function with iterating: {}".format(implement_str2(A,B)))

A = 'aa'
B = 'Aa'
print("function with find method: {} ".format(implement_str1(A,B)))
print("Function with iterating: {}".format(implement_str2(A,B)))

A = ''
B = 'a'
print("function with find method: {} ".format(implement_str1(A,B)))
print("Function with iterating: {}".format(implement_str2(A,B)))

A = 'hello'
B = 'll'
print("function with find method: {} ".format(implement_str1(A,B)))
print("Function with iterating: {}".format(implement_str2(A,B)))




























    

