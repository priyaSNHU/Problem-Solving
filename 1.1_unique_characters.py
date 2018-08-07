#Problem: Implement an algorithm to determine if a string has all unique characters.What if you cannot use an additional data structure.

# method 1
def uniqueCharacters(s):

    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[j] == s[i]:
                return False

#n - number of characters in string
#Time complexity: O(n^2)
#Memory: O(1)

# method 2

def uniqueCharacters(s):

    uc = dict()

    for char in s:
        if char not in s:
            uc[char] = 0
        else:
            return False

#Time complexity: O(n)
#Space Complexity: O(n)
        
    
