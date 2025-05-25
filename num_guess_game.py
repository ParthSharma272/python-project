import random

def get_user_guess(low, high):
    while True:
        guess = int(input(f"Guess a number between {low} and {high}: "))
        if low <= guess <= high:
            return guess
        else:
            print(f"Input out of bounds. Enter a number between {low} and {high}.")


def play_game(low=1, high=10, target_score=5):
    score = 0
    while score < target_score:
        answer = random.randint(low, high)
        guess = get_user_guess(low, high)
        if guess == answer:
            score += 1
            print(f"Correct! The number was {answer}")
            print(f"The current score is :{score}")
        else:
            print(f"Wrong. The number was {answer}")
    print("---------GAME OVER---------")
    print(f"Your final score is {score}")

play_game()
