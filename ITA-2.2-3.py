''' Problem: Consider linear search again (see Exercise 2.1-3). How many elements of the input
sequence need to be checked on the average, assuming that the element being
searched for is equally likely to be any element in the array? How about in the
worst case? What are the average-case and worst-case running times of linear
search in ‚-notation? Justify your answers.
'''

# Time COmplexities:
# BEst CASE: O(1)
# Avg Case: O(n)
# Worst Case: O(n)
def linearSearch(search_ele , lis):
    for i in range(len(lis)):
        if lis[i] == search_ele:
            print("Element Found")

    print("Element not found")


