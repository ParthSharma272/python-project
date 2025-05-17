# x fahrenheit = (float(y degree celsius) * 1.8) + 32
# y degree celsius = float(x fahrenheit) - 32) * 0.5556
# Move the input() for the unit inside the while True loop. Only ask for unit inside the loop. Place the tempconv() call and break after verifying the input is valid. This forces re-prompting until a valid unit is given.

temp = float(input("Enter temperature: "))        
unit = input("Please enter a valid unit (C or F):")

def tempconv(x, y):
    if y == 'C':
        conv = (x * 1.8) + 32
        return f"{x} {y} is equal to {conv} F"
    elif y == 'F':
        conv = (x - 32) * 0.5556
        return f"{x} {y} is equal to {conv} C"
    else:
        return "Invalid Unit" 
       
while unit != 'C' and unit != 'F':
        print("Invalid unit.")
        unit = input("Please enter a valid unit (C or F):")

print(tempconv(temp, unit))
        
        
