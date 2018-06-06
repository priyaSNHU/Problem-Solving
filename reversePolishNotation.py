def reversePolishNotation(expression):
        if len(expression) == 0:
            return 0
        
        stack = []
        for exp in expression:
            if exp not in "+-*/":
                stack.push(exp)
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                
                if exp == "+":
                    stack.push(operand1 + operand2)
                elif exp == "-":
                    stack.push(operand1 - operand2)
                elif exp == "*":
                    stack.push(operand1 * operand2)
                elif exp == "/":
                    stack.append(operand1 / operand2)
        
        result = stack.pop()
        return res
