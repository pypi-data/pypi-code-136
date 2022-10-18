import random
word_list = ['watermelon', 'apple', 'strawberry', 'lemon', 'pear']
word = random.choice(word_list)

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print("You have guessed a letter in the word")
    else:
        print("You have not guessed a letter in the word")

def ask_for_input():
    while True:
        guess = input("Enter a letter: ")
        if len(guess) == 1:
            if guess.isalpha():
                print("You have entered a valid letter")
                break
        else:
            print("You have not entered a valid letter")
    
    check_guess(guess)

ask_for_input()