operations = dict(add=lambda a, b: a + b, sub=lambda a, b: a - b,
                  mul=lambda a, b: a * b, div=lambda a, b: a / b,
                  pow=lambda a, b: a ** b)

def calculator(operator, arg1, arg2):
    global operations
    if operator not in operations:
        raise ValueError("Invalid operation. Available operations: add, sub, mul, div, pow.")
    if not isinstance(arg1, (int, float)) or not isinstance(arg2, (int, float)):
        raise ValueError("Invalid numbers. Second and third arguments must be numerical.")
    else:
        return operations[operator](arg1, arg2)