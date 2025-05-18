import random
import time

game_options = ["rock", "paper", "scissors"]
User_Score = 0
Comp_Score = 0

print("Welcome to Constantinople. The Empire need you. Let's save the City.")

def determine_winner(uc, cc):
    global User_Score, Comp_Score
    if uc == cc:
        print(cc)
        print("The army of God and evil is evenly matched.")
    elif uc == "paper" and cc == "rock":
        print(cc)
        print("Constantinople is safe.")
        User_Score += 1
    elif uc == "paper" and cc == "scissors":
        print(cc)
        print("Constantinople is under Seige.")
        Comp_Score +=1
    elif uc == "rock" and cc == "scissors":
        print(cc)
        print("Constantinople is safe.")
        User_Score += 1
    elif uc == "rock" and cc == "paper":
        print(cc)
        print("Constantinople is under seige.")
        Comp_Score +=1
    elif uc == "scissors" and cc == "paper":
        print(cc)
        print("Constantinople is safe.")
        User_Score += 1
    elif uc == "scissors" and cc == "rock":
        print(cc)
        print("Constantinople is under seige.")
        Comp_Score +=1
    return User_Score, Comp_Score

def win_cond():
    global User_Score, Comp_Score
    if User_Score > Comp_Score:
        print("Constantinople Stands Tall.")
    elif User_Score < Comp_Score:
        print("Constantinople has been lost.")

while True:
    while User_Score < 5 and Comp_Score < 5:
        user_choice = input("Please enter your choice (rock, paper, scissors): ")
        if user_choice not in game_options:
            print("Invalid choice. Try again.")
            continue
        computer_choice = random.choice(game_options)
        determine_winner(user_choice, computer_choice)
        print(f"Your score: {User_Score}")
        print(f"Enemy's score: {Comp_Score}")
    win_cond()
    again = int(input("Press 1 if u want to continue\nPress 2 if u want reset score and play again.\nPress 3 if u want to exit."))
    if again == 1:
        pass
    elif again == 2:
        User_Score = 0
        Comp_Score = 0
    else:
        exit()
     

    



    