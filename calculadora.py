import math

def calculator():
    operation = input("What operation would you like to perform (sqrt, log, log10, sin, cos, tan, asin, acos, atan): ")
    num = float(input("Enter the number: "))
    if operation == 'sqrt':
        print(math.sqrt(num))
    elif operation == 'log':
        base = float(input("Enter the base of the logarithm: "))
        print(math.log(num, base))
    elif operation == 'log10':
        print(math.log10(num))
    elif operation == 'sin':
        print(math.sin(num))
    elif operation == 'cos':
        print(math.cos(num))
    elif operation == 'tan':
        print(math.tan(num))
    elif operation == 'asin':
        print(math.asin(num))
    elif operation == 'acos':
        print(math.acos(num))
    elif operation == 'atan':
        print(math.atan(num))
    else:
        print("Invalid operator")

calculator()
