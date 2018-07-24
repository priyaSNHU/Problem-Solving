def valid_string(s):
    if len(s) == 1:
        print("Yes")
        return
    if s is None:
        print("No")
        return
    str_freq = dict()

    for letter in s:
        if letter in str_freq:
            str_freq[letter] += 1
        else:
            str_freq[letter] = 1

    temp = min(str_freq.values())

    count = 0

    for value in str_freq.values():
        if temp != value:
            count += 1
    if count > 1:
        print("No")
        return
    else:
        print("Yes")
        return


valid_string('s')
valid_string('aa')
valid_string('sl')
valid_string('ssa')
valid_string('sll')
valid_string('abbcc')
