import random

print("Welcome to Number Guessing game (Computer edition)")
num = 0
nums = 0
def guess_num(nums,num):
    num = random.randint(1,101)
    while nums != num:
        nums = int(input("Guess a number between 1 to 100:"))
        if nums not in range(1,101):
            print("Invalid input.")           
        elif nums > num:
            print("Your guess is higher than my Guess.")
        else: 
            print("Your guess is lower than my Guess.")
    print(f"You have guessed it correctly. My guess was {num}.")       
guess_num(nums,num)

  

