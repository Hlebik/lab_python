# postfix_test.py
def calc(expr):
    stack = []
    for x in expr.split():
        print (stack)       
        if x.isdigit():
            stack.append(x)
        else:
            a = stack.pop()
            b = stack.pop()
            if x == '*':
                c = int(a) * int(b)
                stack.append(c)
            if x == '+':
                c = int(a) + int(b)
                stack.append(c)
            if x == '-':
                c = int(b) - int(a)
                stack.append(c)
  
                
    

    return stack[0]

print(calc("1 2 3 * + 2 -"))

import doctest
doctest.testmod()
