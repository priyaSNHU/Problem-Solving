##Problem:Given 2 strings A and B (both uppercase), you can only remove characters from A. Return “Yes”/”No”. 


def string_match(s1,s2):
    if len(s1) < len(s2):
        print("No")
        return
    if len(s1) == 0 or len(s2) == 0:
        print("No")
        return
    if len(s1) == len(s2):
        if s1 == s2:
            print("Yes")
            return
        else:
            print("No")
            return
    else:
        s1_comb = get_all_comb_strings(s1)

        for sub_str in s1_comb:
            if len(sub_str) == len(s2) and sub_str == s2:
                print("Yes")
                return
            else:
                print("No")
                return


def get_all_comb_strings(s1):
    return [s1[i : j + 1] for i in range(len(s1)) for j in range(i , len(s1))]

string_match('AB' , 'AC')
string_match('a' , 'A')
