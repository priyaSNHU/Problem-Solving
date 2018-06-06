def polishNotation(expression):
    s = stack()
    result = 0
    for exp in range(0, len(expression)-1):
        exp_list.append(exp)

    reverse_exp_list = exp_list[::-1]
    temp = 0

    for item in reverse_exp_list:
        if item == "+":
            operand1 = s.pop()
            operand2 = s.pop()
            result = operand1 + operand2
            s.push(result)
        elif item == "-":
            operand1 = s.pop()
            operand2 = s.pop()
            result = operand1 - operand2
            s.push(result)
        elif item == "*":
            operand1 = s.pop()
            operand2 = s.pop()
            result = operand1 * operand2
            s.push(result)
        elif item == "/":
            operand1 = s.pop()
            operand2 = s.pop()
            result = operand1 / operand2
            s.push(result)
        elif item is in [0123456789]:
            s.push(item)
        else:
            print("Invalid input")

    if len(s) == 1:
        return s.peek()
    
        
