'''Problem: Referring back to the searching problem (see Exercise 2.1-3), observe that if the
sequence A is sorted, we can check the midpoint of the sequence against  and
eliminate half of the sequence from further consideration. The binary search algorithm
repeats this procedure, halving the size of the remaining portion of the
sequence each time. Write pseudocode, either iterative or recursive, for binary
search. Argue that the worst-case running time of binary search is ‚.lg n/.

'''

# Time Complexity:
#avg and worst cases: O(log n) + O(log n) => O(log n)
# Best Case: O(1)
# Space Complexity: O(n)

# find the element in the array
def binary_search(arr , target_value):
    if arr is None:
        return 'Not Found'
    elif target_value < arr[0] or target_value > arr[-1]:
        return 'Given value is not present in the array'
    mid = len(arr)//2
    if arr[mid] == target_value:
        return 'Found'
    elif arr[mid] > target_value:
        return binary_search(arr[0:mid] , target_value)
    elif arr[mid] < target_value:
        return binary_search(arr[mid+1:] , target_value)
    

# input for length of an array
print('Enter the length of an array: ')
len_arr = int(input())
arr = []
print('Enter the array elements: ')
for i in range(len_arr):
    i = int(input())
    arr.append(i)
print('unsorted array')
print(arr)
arr = sorted(arr)
print('sorted arr')
print(arr)
# get the input to search an element in an array
print('Enter the element to search: ')
target_value = int(input())
# find the element in given array
print(binary_search(arr , target_value))
