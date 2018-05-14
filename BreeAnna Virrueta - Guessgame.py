import random
# BreeAnna Virrueta
# 1) Generate Random Number
# 2) Take an input (number) from the user
# 3) Compare input to generated number
# 4) Add "Higher" or "Lower" statements
# 5) Add 5 guesses

number = random.randint(1, 50)
# print(number)


guess = input("What is your guess? ")


# Initializing Variables
answer = random.randint(1, 50)
turns_left = 5
correct_guess = False

# This describes ONE turn (This is the game controller)
while turns_left > 0 and correct_guess is False:
    guess = int(input("Guess a number between 1 and 50: "))

    if guess == answer:
        print("You win!")
        correct_guess = True
    elif guess > answer:
        print("Too high!")
        turns_left -= 1
    elif guess < answer:
        print("Too low!")
        turns_left -= 1
