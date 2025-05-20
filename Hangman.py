import random
import string
words = ["apple", "banana", "mango", "strawberry", "orange", "grape", "pineapple", "apricot", "lemon", "coconut", "watermelon", "cherry", "papaya", "berry", "peach", "lychee", "muskmelon"]

word = random.choice(words).upper()
print("Welcome to the Hangman game.")        


def hangman():
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    
    while len(word_letters) > 0:
        print("You have used these letters",' '.join(used_letters))
        
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word:',' '.join(word_list))
        
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")

        else:
            print("Invalid character.")
    print("You guessed the word", word)

hangman()



