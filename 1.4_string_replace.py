def str_replace(string, n):
    new_index = len(string)

    for i in reversed(range(n)):
        if string[i] == ' ':
            # Replace spaces
            string[new_index - 3:new_index] = '%20'
            new_index -= 3
        else:
            # Move characters
            string[new_index - 1] = string[i]
            new_index -= 1

    return string


s1 = "Mr John Smith   "
print(str_replace(s1 , 13))
