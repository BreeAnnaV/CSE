import random
import string
"""
A general guide for Hangman
1. Make a word bank - 10 items
2. Pick a random item from the list
3. Add a guess to the list of letters guessed Hide the word (use *) (letters_guessed = [...])
4. Reveal letters already guessed
5. Create the win condition

"""
guesses_left = 10

word_bank = ["Environment", "Xylophone", "LeBron James", "Kobe", "Jordan", "Stephen Curry", "Avenue", "Galaxy",
             "Snazzy", "The answer is two"]
word_picked = (random.choice(word_bank))
letters_guessed = []
random_word = len(word_picked)
# print(word_picked)
guess = ''
correct = random.choice

while guess != "correct":
    guess = ()
    for letter in word_picked:
        if letter is letters_guessed:
            print()
