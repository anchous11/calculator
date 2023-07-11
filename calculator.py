import math
def calculator(expression):
    try:
        result = eval(expression)
        return result
    except (SyntaxError, TypeError):
        return "Wrong expression"
    except ZeroDivisionError:
        return "Division by zero"

expression = input("Enter your expression: ")
print('{} = '.format(expression))
print(calculator(expression))
