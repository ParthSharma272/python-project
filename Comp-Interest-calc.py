#Compoud Interest formula = A = P(1 + r/n)^(nt)
# A = Final amount (float)
# P = Principal amount(initial investment) (float)
# r = Annual Interest rate (float)
# n = Number of times interest applied per time period (int)
# t = no of years the of the compounding (int)

#principal = float(input("Enter the amount of your initial investment:"))
#rate = float(input("Enter the rate of interest:"))
#num = int(input("Enter the number of times interest is applied per year:"))
#time = float(input("Enter the number of years the money is invested for:"))
#def comp_calc(pr, r, n, t):
#    A = pr * ((1 + r*(n/100))**(n*t))
#    return A
#result = comp_calc(principal, rate, num, time)
#print(f"The final amount after {time} years is: {result}")

principal = 0
rate = 0
num = 0
time = 0
# Using While Loops 
while True:
    principal = float(input("Enter the amount of your initial investment:"))
    if principal < 0:
        print("Please enter a positive number for the principal amount.")
    else:
        break
while True:
    rate = float(input("Enter the rate of interest:"))
    if rate < 0:
        print("Please enter a positive number for the rate of interest:")
    else:
        break
while True:
    num = int(input("Enter the number of times interest is applied per year:"))
    if num < 0:
        print("Please enter a positive number for the number of times interest is applied per year:")
    else:
        break
while True:
    time = int(input("Enter the number of years the money is invested for:"))
    if time < 0:
        print("Please enter a positive number for the number of years the money is invested for:")
    else:
        break
        
result = principal * ((1 + rate*(num/100))**(num*time))
print(f" Your final amount after {time} years is: {result}")