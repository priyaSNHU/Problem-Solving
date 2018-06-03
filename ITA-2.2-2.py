###### Problem: Consider sorting n numbers stored in array A by first finding the smallest element
##of A and exchanging it with the element in AŒ1. Then find the second smallest
##element of A, and exchange it with AŒ2. Continue in this manner for the first n1
##elements of A. Write pseudocode for this algorithm, which is known as selection
##sort. What loop invariant does this algorithm maintain? Why does it need to run
##for only the first n  1 elements, rather than for all n elements? Give the best-case
##and worst-case running times of selection sort in ‚-notation. 


##selection sort Pseodocode:
##
##for i = len(lis)-1 to 0:
##    min_num = i
##    for j = i+1 to len(lis):
##        if lis[min_num] > lis[j]:
##            min_num = j
##    lis[i], lis[min_num] = lis[min_num], lis[i]

# Time COmplexities:
# BestCase: O(n^2)-comparisions
#worstCase: O(n^2)-comparisions


def selectionSort(lis):
    for i in range(len(lis)):
        min_index = i
        for j in range( i+1, len(lis)):
            if lis[min_index] > lis[j]:
                min_index = j

        lis[i], lis[min_index] = lis[min_index], lis[i]


n = int(input())
arr = input()   # takes the whole line of n numbers
l = list(map(int,arr.split(' ')))


    
