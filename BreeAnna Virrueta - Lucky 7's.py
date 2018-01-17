import random
# BreeAnna Virrueta
# 1)Generate 2 random numbers between 1 and 6
# 2) Print 2 numbers on line below that
# 3) Add the numbers together to get your total
# 4) Print the sum on the line below

money = 15
rounds = 0

while money > 0:
    money -= 1
    dice1 = (random.randint(1, 6))
    dice2 = (random.randint(1, 6))
    total = dice1 + dice2
    print("You rolled a %s" % dice1)
    print("You also rolled a %s" %dice2)
    print("Your total is %s" % total)
    print("Your current amount of money is %s" % money)
    if total == 7:
        rounds += 1
        money += 5
        print("You win")
        print("Your current total is now %s" % money)
    if total > 7:
        rounds += 1
        print("You lose")
    if total < 7:
        rounds += 1
        print("You lose")
    if money == 0:
        print("Game is over, you cannot continue playing")
        print("You ended the game with %s rounds" % rounds)