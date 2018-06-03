''' Problem: We can express insertion sort as a recursive procedure as follows. In order to sort
AŒ1 : : n, we recursively sort AŒ1 : : n 1 and then insert AŒn into the sorted array
AŒ1 : : n  1. Write a recurrence for the running time of this recursive version of
insertion sort. '''

# recurrence:
#O(1) if length of input is 1
# T(n-1) + O(n) if the input of length is greater than 1

def insertionSort(lis , start = 1):
    if not lis:
        return None
    elif len(lis) == 1:
        return lis

    if lis[start-1] > lis[start]:
        temp = lis[start]
        for i in range(0,start):
            if temp < lis[start]:
                lis.insert(i , temp)
                del lis[start+1]
                break
    return insertionSort(lis, start + 1)
    
