#Leetcode:

def romanint(s):
    roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    result = 0
    if not S:
        return "No values Present"

    if type(s) != str:
        return "Invalid Type"
    for i in range(len(s)-1):
        if s[i] in roman_dict:
            if roman_dict[s[i]] < roman_dict[s[i+1]]:
                result -= roman_dict[s[i]]
            else:
                result += roman_dict[s[i]]
        else:
            return "Invalid Roman Values"
    return result + roman_dict[s[-1]]


#Test Cases

S = "XI"
print("Integer value for Roman {} is : {}".format(S, romanint(S)))

S = "IX"
print("Integer value for Roman {} is : {}".format(S, romanint(S)))

S = "IV"
print("Integer value for Roman {} is : {}".format(S, romanint(S)))

S = "VI"
print("Integer value for Roman {} is : {}".format(S, romanint(S)))

S = "LVIII"
print("Integer value for Roman {} is : {}".format(S, romanint(S)))

S = "MCMXCIV"
print("Integer value for Roman {} is : {}".format(S, romanint(S)))

S = "123"
print("Integer value for Roman {} is : {}".format(S, romanint(S)))

S = ""
print("Integer value for Roman {} is : {}".format(S, romanint(S)))

S = 1
print("Integer value for Roman {} is : {}".format(S, romanint(S)))


