## Problem link: https://www.hackerrank.com/challenges/abbr/problem


def string_match(s1,s2):
    if len(s1) < len(s2):
        print("No")
        return
    if len(s1) == 0 or len(s2) == 0:
        print("No")
        return
    if len(s1) == len(s2):
        if s1.upper() == s2:
            print("Yes")
            return
        else:
            if s1 == s2:
                print("Yes")
                return
            else:
                print("No")
                return           
    if s1[0].isupper():
        if s1[0] == s2[0]:
            return string_match(s1[1:],s2[1:])
        else:
            print("No")
            return  
    else:
        if s1[0].upper() != s2[0]:
            return string_match(s1[1:],s2)
        else:
            return (string_match(s1[1:],s2[1:]) or string_match(s1[1:],s2))

