class Characters(object):
    def __init__(self, name, description, inventory, abilities, health):
        self.name = name
        self.description = description
        self.inventory = inventory
        self.abilities = abilities
        self.health = health
        self.spaces = 0

    def move(self):
        if self.abilities:
            print("The character moves closer to you.")
        else:
            print("Nothing happens.")

    def move_forward(self, spaces):
        self.spaces = spaces
        self.move()
        print("It moves forward %s spaces." % spaces)


character = Characters("Boo", "Black and Blue", "Has a sword", True, "20 bars")
character.move_forward(2)
