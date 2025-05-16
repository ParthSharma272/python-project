num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")
def calc(x, y, o):
    if o == '+':
        return x + y
    elif o == '-':
        return x - y
    elif o == '*':
        return x * y
    elif o == '/':
        if y == 0:
            return "Error: Division by zero"
        else:
            return x / y
    else:
        return "Invalid operation"
result = calc(num1, num2, operation)
print(f"The result of {num1} {operation} {num2} is: {result}")