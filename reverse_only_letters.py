#Problem: https://leetcode.com/problems/reverse-only-letters/

# Time complexity: O(N)
# Memory complexity: O(N)
#Method 1:
def reverse_letters(s):
    chars = []
    reverse_letters = []
    for ch in s:
        if ch.isalpha():
            chars.append(ch)

    for ch in s:
        if ch.isalpha():
            reverse_letters.append(chars.pop())
        else:
            reverse_letters.append(ch)

    return ''.join(reverse_letters)
            

# Time complexity: O(N)
# Memory complexity: O(N)
#Method 2:
def rev_letters(s):
    i = 0
    j = len(s) - 1
    letters = list(s)
    #print(letters)
    while i <= j:
        if letters[i].isalpha() and letters[j].isalpha():
            letters[i], letters[j] = letters[j], letters[i]
            i += 1
            j -= 1
        elif not letters[i].isalpha():
            i += 1
        elif not letters[j].isalpha():
            j -= 1
    return ''.join(letters)


print(reverse_letters('ab-cd'))
print(rev_letters('ab-cd'))
            
