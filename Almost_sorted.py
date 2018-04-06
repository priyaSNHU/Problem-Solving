# HACKERRANK PROBLEM LINK: https://www.hackerrank.com/challenges/almost-sorted/problem
# Sorting problem
def Cons_sort(arr):
    sort_arr = sorted(arr)
    unsorted_elements = []
    for i in range(len(arr)):
        if arr[i] != sort_arr[i]:
            unsorted_elements.append(i+1)
    if len(unsorted_elements) == 0:
        print("yes")
    if len(unsorted_elements) == 1:
        print("no")
    elif len(unsorted_elements) == 2:
        print("yes \nswap",  unsorted_elements[0]  , unsorted_elements[-1])
    else:
        sub_arr = arr[unsorted_elements[0]-1: unsorted_elements[-1]]
        if sorted(sub_arr) == sub_arr[::-1]:
            print("yes \nreverse" , unsorted_elements[0], unsorted_elements[-1])
        else:
            print("no")


               
        
        
