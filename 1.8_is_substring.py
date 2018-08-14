#Problem: Assume you have a method isSubstring which checks if one word is a substring of another. Given two Strings, check if s2 is a rotation of s1using only one call to isSubstring

def is_substring(string1 , string2):
    if string1 == None or string2 == None:
        return
    if len(string1) != len(string2)or len(string1) == 0:
        return
    substring = string1 + string1
    if string2 in substring:
        return True
    else:
        return False

