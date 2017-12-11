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










while guess:
    if guess > random:
        print("Lower")
    elif guess < random:
        print("Higher")
    else: guess == random
    print("Correct!")

