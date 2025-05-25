menu = {"pizza" : 3.25,
        "pretzel" : 2.90,
        "bread" : 1.85,
        "spaghetti": 2.15,
        "shawarma": 3.45,
        "french fries": 2.20,
        "nachos": 2.35,
        "popcorn": 6.00}

cart = []
total = 0
print("--------MENU--------")
print()
for key,value in menu.items():
    print(f"{key:15}:${value:.2f}")
    print()
print()
print("--------------------")

while True:
    food = input("Enter a food item to buy(Press q to quit):").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        

    
for food in cart:
    print(food)
    total += menu.get(food)    

print(f"Your total bill is :{total}")