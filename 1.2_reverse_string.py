#problem: Implement a fucntionwhich reverse a null terminating string

def revStr(s):
    s = list(s)
    for i in range(len(s)//2):
        s[-i-1] , s[i] = s[i], s[-i-1]

    rev_string = "".join(s)

    return rev_string


print(revStr("i love prudhvi"))

#Time COmplexity: O(n) - n  is number of characters in a string
# Memory : O(n) - size of list


        
