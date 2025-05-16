#2.20462
#0.453592
weight = float(input("Enter weight: "))
unit = input("Enter unit (kg or lb): ")
def kgtolb(x):
    return x * 2.20462
def lbtokg(x):
    return x * 0.453592
if unit == 'kg':
    result = kgtolb(weight)
    print(f"{weight} kg = {result}lbs")
elif unit == 'lb':
    result = lbtokg(weight)
    print(f"{weight} lb = {result} kgs")
else:
    print("Invalid Unit")
