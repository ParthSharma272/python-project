# x fahrenheit = (float(y degree celsius) * 1.8) + 32
# y degree celsius = float(x fahrenheit) - 32) * 0.5556

temp = float(input("Enter temperature: "))
unit = input("Enter unit (C or F):")

def tempconv(x, y):
    if y == 'C':
        conv = (x * 1.8) + 32
        return f"{x} {y} is equal to {conv} F"
    elif y == 'F':
        conv = (x - 32) * 0.5556
        return f"{x} {y} is equal to {conv} C"
    else:
        return "Invalid Unit" 
        
result = tempconv(temp, unit)
print(result)