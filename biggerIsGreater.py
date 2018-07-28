#Probem: https://www.hackerrank.com/challenges/bigger-is-greater/problem

def biggerIsGreater(s):
    is_greater = False
    for i in range(len(s)-1)[::-1]:
        # check if the previous letter is greater than successor letter
        if ord(s[i]) < ord(s[ i + 1 ]):
            for j in range(i + 1 , len(s))[::-1]:
                if ord(s[i]) < ord(s[j]):
                    str_lis = list(s)
                    str_lis[i],str_lis[j] = str_lis[j],str_lis[i]
                    print("".join(str_lis[: i + 1 ] + str_lis[i + 1 : ][::-1]))
                    is_greater = True
                if is_greater == True:
                    break
        if is_greater == True:
            break
    if is_greater == False:
        print("no answer")


s = 'ab'
s = 'aa'
s = 'abc'
s = 'Cba'
s = 'Aa'
s = 'cba'
s = 'a'
biggerIsGreater(s)
