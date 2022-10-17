import random 

word_list = ['watermelon', 'apple', 'strawberry', 'lemon', 'pear']
word = random.choice(word_list)
print(word)
guess = input("Enter a letter: ")
if len(guess) == 1:
    if guess.isalpha():
        print("You have entered a valid letter")