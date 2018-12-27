# LeetCode: https://leetcode.com/problems/integer-to-roman/

def ConvertIntRoman(num):
    
    roman = []
    while num > 0:
        if num - 1000 >= 0:
            num -= 1000
            roman.append("M")
        elif num - 900 >= 0:
            num -= 900
            roman.append("CM")
        elif num - 500 >= 0:
            num -= 500
            roman.append("D")
        elif num - 400 >= 0:
            num -= 400
            roman.append("CD")
        elif num - 100 >= 0:
            num -= 100
            roman.append("C")
        elif num-90 >= 0:
            num -= 90
            roman.append("XC")
        elif num - 50 >= 0:
            num -= 50
            roman.append("L")
        elif num - 40 >= 0:
            num -= 40
            roman.append("XL")
        elif num - 10 >= 0:
            num -= 10
            roman.append("X")
        elif num - 9 >= 0:
            num -= 9
            roman.append("IX")
        elif num - 5 >= 0:
            num -= 5
            roman.append("V")
        elif num - 4 >= 0:
            num -= 4
            roman.append("IV")
        else:
            num -= 1
            roman.append("I")
    return ''.join(roman)

def convertIntRoman(num):
    if num < 0 or type(num) != int:
        return 
    roman_dict = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1}
    result = ""
    for roman, value in roman_dict.items():
        while num >= value:
            num -= value
            result += roman

    return result

#Test cases

num = -1
print("Integer value for Roman {} inum : {}".format(num, ConvertIntRoman(num)))
print("2nd Approach")
print("Integer value for Roman {} inum : {}".format(num, convertIntRoman(num)))


num = 34
print("Integer value for Roman {} inum : {}".format(num, ConvertIntRoman(num)))
print("2nd Approach")
print("Integer value for Roman {} inum : {}".format(num, convertIntRoman(num)))

num = 99
print("Integer value for Roman {} inum : {}".format(num, ConvertIntRoman(num)))
print("2nd Approach")
print("Integer value for Roman {} inum : {}".format(num, convertIntRoman(num)))

num = 3
print("Integer value for Roman {} inum : {}".format(num, ConvertIntRoman(num)))
print("2nd Approach")
print("Integer value for Roman {} inum : {}".format(num, convertIntRoman(num)))

num = 4
print("Integer value for Roman {} inum : {}".format(num, ConvertIntRoman(num)))
print("2nd Approach")
print("Integer value for Roman {} inum : {}".format(num, convertIntRoman(num)))

num = 9
print("Integer value for Roman {} inum : {}".format(num, ConvertIntRoman(num)))
print("2nd Approach")
print("Integer value for Roman {} inum : {}".format(num, convertIntRoman(num)))

num = 13
print("Integer value for Roman {} inum : {}".format(num, ConvertIntRoman(num)))
print("2nd Approach")
print("Integer value for Roman {} inum : {}".format(num, convertIntRoman(num)))

num = 1994
print("Integer value for Roman {} inum : {}".format(num, ConvertIntRoman(num)))
print("2nd Approach")
print("Integer value for Roman {} inum : {}".format(num, convertIntRoman(num)))

num = 98
print("Integer value for Roman {} inum : {}".format(num, ConvertIntRoman(num)))
print("2nd Approach")
print("Integer value for Roman {} inum : {}".format(num, convertIntRoman(num)))

num = 40
print("Integer value for Roman {} inum : {}".format(num, ConvertIntRoman(num)))
print("2nd Approach")
print("Integer value for Roman {} inum : {}".format(num, convertIntRoman(num)))























            
