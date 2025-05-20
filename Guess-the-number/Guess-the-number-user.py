import random
print("Welcome to Number Guessing game (Human edition)")

def guess_num(x):
    low = 1
    high = x
    ask = ""
    while ask != "correct":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        print(f"My guess was {guess}")
        ask = input("Is it high or low or correct?:").lower()
        if ask == "high":
            high = guess - 1
        elif ask == "low":
            low = guess + 1
    print(f"Yay. I guessed your number correctly. It is {guess}.")            

guess_num(100)