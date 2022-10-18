import random

class Hangman:
    def __init__(self, num_lives, word_list):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in range(len(self.word))]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = letter
            self.num_letters -= 1
        else:
            print(f"Sorry, {guess} is not in the word.")
            # print(f"You have {self.num_lives} lives left.")
            self.num_lives -= 1
    
    def ask_for_input(self):
        while True:
            guess = input("Enter a letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

def play_game():
    word_list= ['watermelon', 'banana', 'apple', 'orange', 'strawberry', 'pineapple', 'grape', 'kiwi', 'pear', 'mango', 'blueberry', 'raspberry', 'blackberry', 'cherry', 'lemon', 'lime', 'coconut', 'avocado', 'peach', 'plum', 'apricot', 'nectarine', 'cantaloupe', 'honeydew', 'watermelon', 'papaya', 'persimmon', 'fig', 'pomegranate', 'grapefruit', 'tangerine', 'mandarin', 'jackfruit', 'durian', 'lychee', 'starfruit', 'tomato', 'cucumber', 'eggplant', 'pepper', 'potato', 'onion', 'garlic', 'ginger', 'carrot', 'broccoli', 'cauliflower', 'cabbage', 'spinach', 'kale', 'lettuce', 'asparagus', 'celery', 'mushroom', 'zucchini', 'squash', 'corn', 'bean', 'pea', 'artichoke', 'sweet potato', 'yam', 'pumpkin', 'radish', 'beet', 'turnip', 'sweetcorn', 'okra', 'brussels sprout', 'cress', 'horseradish', 'wasabi', 'rhubarb', 'cucumber', 'aubergine', 'avocado', 'bell pepper', 'broccoli', 'brussels sprout', 'cabbage', 'carrot', 'cauliflower', 'celery', 'chilli pepper', 'corn', 'cucumber', 'eggplant', 'garlic', 'ginger', 'kale', 'leek', 'lettuce', 'mushroom', 'onion', 'pea', 'potato', 'pumpkin', 'radish', 'spinach', 'sweet potato', 'tomato', 'turnip', 'watercress', 'zucchini', 'apple', 'apricot', 'avocado', 'banana', 'blackberry', 'blueberry', 'cherry', 'coconut', 'fig', 'grape', 'grapefruit', 'kiwi', 'lemon', 'lime', 'mango', 'orange', 'papaya']
    game = Hangman(word_list, 5)
    while True:
        game.ask_for_input()
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters == 0:
            print("You won!")
            break
