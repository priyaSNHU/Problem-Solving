#Problem: Given 2 strings determine whether given strings are permutation of other string

def perm_str(s1,s2):
    if len(s1) != len(s2):
        return False

    if sorted(s1) == sorted(s2):
        return True
    else:
        return False


# TIme COmplexity: O(nlogn)
# Memory: O(1)

def perm_str(s1,s2):
    if len(s1) != len(s2):
        return False

    perm_str = dict()

    for char in s1:
        if char not in s1:
            perm_str[char] = 1
        else:
            perm_str[char] += 1
    # If character in s2 is fond in dict then reduce char value to -1
    for char in s2:
        if char in s2:
            perm_str[char] -= 1
        else:
            return False

    # Check if any value key is grater than 0
    for key in perm_str:
        if perm_str[key][0] > 0:
            return False
        else:
            return True

# TIme COmplexity: O(n)
            
            


