rows = int(input("Enter the number of rows:"))
cols = int(input("Enter the number of columns:"))
symbol = input("Enter the symbol to use for the rectangle:")

while rows > 1 or cols > 1:
    for x in range(rows):
        for y in range(cols):
            print(symbol, end ="")
        print()
print("Please enter a number larger than 2 for the number of rows and columns.")