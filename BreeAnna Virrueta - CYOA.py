# items -> characters -> rooms
# instantiate classes


class Item(object):
    def __init__(self, name):
        self.name = name

    def drop_item(self):
        print("You drop %s" % self.name)


class Toy(Item):
    def __init__(self, name):
        super(Toy, self).__init__(name)

    def play(self):
        print("You play with the %s." % self.name)


class StuffedRabbit(Toy):
    def __init__(self):
        super(StuffedRabbit, self).__init__(name="stuffed rabbit")

    def collect_animal(self):
        print("You take the %s." % self.name)


test_stuffed = StuffedRabbit()


class ActionFigure(Toy):
    def __init__(self):
        super(ActionFigure, self).__init__(name="action figure")

    def collect_figure(self):
        print("You take the %s action figure." % self.name)


test_figure = ActionFigure()


class JoyStick(Toy):
    def __init__(self):
        super(JoyStick, self).__init__(name="joystick")

    def collect_joystick(self):
        print("You pick up the joystick. This may come in handy later.")


test_joystick = JoyStick()


class Clothing(Item):
    def __init__(self, name):
        super(Clothing, self).__init__(name)

    def wear(self):
        print("You wear the %s." % self.name)


class Shirt(Clothing):
    def __init__(self):
        super(Shirt, self).__init__(name="shirt")

    def collect_shirt(self):
        print("You take the %s." % self.name)


test_shirt = Shirt()


class Pants(Clothing):
    def __init__(self):
        super(Pants, self).__init__(name="pants")

    def collect_pants(self):
        print("You take the %s." % self.name)


test_pants = Pants()
# test_pants.wear()
# test_pants.collect_pants()


class Shoes(Clothing):
    def __init__(self):
        super(Shoes, self).__init__(name="shoes")

    def collect_shoes(self):
        print("You take the %s." % self.name)


test_shoes = Shoes()
# test_shoes.collect_shoes()
# test_shoes.wear()


class Hat(Clothing):
    def __init__(self):
        super(Hat, self).__init__(name="hat")

    def collect_hat(self):
        print("You take the %s." % self.name)


test_hat = Hat()
# test_hat.collect_hat()
# test_hat.wear()


class HockeyPuck(Item):
    def __init__(self):
        super(HockeyPuck, self).__init__(name="hockey puck")

    def collect_puck(self):
        print("You pick up the hockey puck. This may come in handy later.")


test_puck = HockeyPuck()


class MiniGolfBall(Item):
    def __init__(self):
        super(MiniGolfBall, self).__init__(name="golf balls")

    def collect_ball(self):
        print("You pick up the mini golf ball. This may come in handy later.")


test_golf = MiniGolfBall()


class CarKey(Item):
    def __init__(self):
        super(CarKey, self).__init__(name="key")

    def collect_key(self):
        print("You pick up the car key. This may come in handy later.")


test_key = CarKey()


class SteeringWheel(Item):
    def __init__(self):
        super(SteeringWheel, self).__init__(name="steering wheel")

    def collect_wheel(self):
        print("You pick up the steering wheel. This may come in handy later.")


test_wheel = SteeringWheel()


class WelcomeLetter(Item):
    def __init__(self, words):
        super(WelcomeLetter, self).__init__(name="Welcome Letter")
        self.words = words

    def read_letter(self):
        print("You read the letter. %s" % self.words)


test_letter = WelcomeLetter('Welcome to the game. The goal is to collect everything you can and '
                            'put it into a case you at the Center of the Mall. If you do not '
                            'find everything, you will not be able to win the game. If you are '
                            'able to collect everything, you win the game. Along the way you '
                            'will discover many other fun activities to do. Good Luck.')


class Basketball(Item):
    def __init__(self):
        super(Basketball, self).__init__(name="basketball")

    def throw_ball(self):
        print("You hit someone. Run!")


test_ball = Basketball()


class Weapon(Item):
    def __init__(self, name, durability):
        super(Weapon, self).__init__(name)
        self.durability = durability

    def attack(self):
        print("You hit something.")
        self.durability = ('%s' % self.durability)


test_weapon = Weapon


class Bat(Weapon):
    def __init__(self):
        super(Bat, self).__init__(name="bat",
                                  durability=100)

    def collect_bat(self):
        print("You take the bat with %s durability." % self.durability)


test_bat = Bat()
# test_bat.collect_bat()
# test_bat.attack()


class HockeyStick(Weapon):
    def __init__(self):
        super(HockeyStick, self).__init__(name="hockey stick",
                                          durability=100)

    def collect_stick(self):
        print("You take the hockey stick with %s durability." % self.durability)


test_stick = HockeyStick()


class Wrench(Weapon):
    def __init__(self):
        super(Wrench, self).__init__(name="wrench",
                                     durability=100)

    def collect_wrench(self):
        print("You take the wrench with %s durability" % self.durability)


test_wrench = Wrench()


class Consumable(Item):
    def __init__(self, name, price):
        super(Consumable, self).__init__(name)
        self.price = price


class CornDog(Consumable):
    def __init__(self):
        super(CornDog, self).__init__(name="corn dog",
                                      price=2)

    def eat_corndog(self):
        print("You eat the %s." % self.name)


test_dog = CornDog()
# test_dog.buy()


class Soda(Consumable):
    def __init__(self):
        super(Soda, self).__init__(name="soda",
                                   price=4)

    def drink_soda(self):
        print("You take a sip of the %s." % self.name)


test_soda = Soda()


class Salad(Consumable):
    def __init__(self):
        super(Salad, self).__init__(name="salad",
                                    price=7)

    def eat_salad(self):
        print("You eat the %s." % self.name)


test_salad = Salad()


class Candy(Consumable):
    def __init__(self):
        super(Candy, self).__init__(name="candy",
                                    price=2)

    def eat_candy(self):
        print("You eat the %s." % self.name)


test_candy = Candy()
# test_candy.buy()


class Characters(object):
    def __init__(self, name, description, inventory, ability):
        self.name = name
        self.description = description
        self.inventory = inventory
        self.ability = ability
        self.spaces = 0

    def move(self):
        if self.ability:
            print("You move.")
        else:
            print("Nothing happens.")

    def move_forward(self, spaces):
        self.spaces = spaces
        self.move()
        print("%s move forward %s spaces." % (self.name, spaces))

    def spawn(self):
        print("%s spawn in the world." % self.name)


boy = Characters("The little boy", "He is holding something.", ActionFigure, False)
you = Characters("You", None, True, True)


class Room(object):
    def __init__(self, name, description, north, west, east, south, left, right, leave, item, characters):
        self.name = name
        self.description = description
        self.north = north
        self.west = west
        self.east = east
        self.south = south
        self.left = left
        self.right = right
        self.leave = leave
        self.item = item
        self.characters = characters

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


CENTER = Room("Center of the Mall", "You are outside a huge shopping center. There is a letter in your hand.", 'KIDS',
              'FOOD', 'ARCADE', None, None, None, None, [WelcomeLetter], None)
FOOD = Room("Food Court", "You are inside. You see many different restaurants. Order a corn dog, soda, salad, or candy."
                          "", 'CLOTHES', 'GOLF', 'CENTER', 'RESTROOMS', None, None, None, [CornDog(), Salad(), Soda(),
                                                                                           Candy()], None)
RESTROOMS = Room("Restrooms", "There are two doors. One leading to the female room, the other to the male room. Go "
                              "left or right.", 'FOOD', None, None, None, 'MEN', 'WOMEN', None, None, None)
WOMEN = Room("Women Restroom", "There is nobody in here. There is a door leading south.", None, None, None, 'PARKING',
             None, None, 'RESTROOMS', None, None)
MEN = Room("Men Restroom", "You see someone in the corner. You could go up to them, or go south.", None,
           None, None, 'PARKING', None, None, 'RESTROOMS', [ActionFigure()], boy)
PARKING = Room('Parking Garage', "You are outside, behind the mall. There is a shiny key on the ground. "
                                 "You see a door pretty far from you leading back inside.", 'RESTROOMS', 'GARAGE',
               'BASKETBALL', None, None, None, None, [CarKey()], None)
GOLF = Room("Mini Golf Course", "You are in a slightly lit room with many people waiting in a line. You see golf "
                                "balls.", None, None, 'FOOD', 'GARBAGE', None, None, None, [MiniGolfBall()], None)
GARBAGE = Room("Dumpsters", "There is a terrible smell coming from the dumpsters. You see something that catches your "
                            "attention. It's a sterring wheel...", 'GOLF', None, 'PARKING', None, None, None, None,
               [SteeringWheel()], None)
BASKETBALL = Room("Basketball Courts", "Basketballs are flying everywhere and you are trying your best not to get hit."
                                       "If you get one you can throw it at someone, or your only way out is through a "
                                       "door to the north.", 'SPORTS', 'PARKING', None, None, None, None, None,
                  [Basketball()], None)
SPORTS = Room("Sports Center", "There are multiple hallways in front of you. You also see a hockey puck just sitting "
                               "on the ground.", 'ARCADE', 'BAT', 'ICE', 'BASKETBALL', None, None, None, [HockeyPuck()],
              None)
ICE = Room("Ice Rink", "All of a sudden it gets extremely cold. People are playing hockey on the ice. You see a "
                       "hockey stick next to you.", None, 'SPORTS', 'SWIM', None, None, None, None, [HockeyStick()],
           None)
BAT = Room('Batting Cage', "You have been looking for a new bat. There is one in front of you.", None, None, 'SPORTS',
           None, None, None, None, [Bat()], None)
SWIM = Room("Swimming Pools", "The room is full of pools.", None, 'ICE', None, None, None, None, None, None, None)
CLOTHES = Room("Clothing Stores", "The stores are flooded with people, but it is your lucky day, you are already "
                                  "wearing clothes!", None, None, 'KIDS', 'FOOD', None, None, None, [Shirt(), Pants(),
                                                                                                     Shoes(), Hat()],
               None)
KIDS = Room("Kids Area", "You are outside and you see a stuffed rabbit on the ground. Kids are running around and you "
                         "hear a huge crash. To the east you see cars.", None, 'CLOTHES', 'RACE', 'CENTER', None, None,
            None, [StuffedRabbit()], None)
RACE = Room("Race Track", "A huge track is in front of you. You should take the wrench on the ground", None, 'KIDS',
            None, None, None, None, None, [Wrench()], None)
ARCADE = Room("Arcade", "A room full of retro machines and new gadgets. There is a joystick on the ground.", None,
              'CENTER', None, 'SPORTS', None, None, None, [JoyStick()], None)


center_node = Room("Center of the Mall", "You are outside a huge shopping center. There is a letter in your hand.",
                   'KIDS', 'FOOD', 'ARCADE', None, None, None, None, WelcomeLetter, you)


current_node = center_node
directions = ['north', 'west', 'east', 'south', 'left', 'right', 'leave', 'order']
short_directions = ['n', 'w', 'e', 's']
inventory = []

while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_').lower()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        # Look for which command we typed in
        pos = short_directions.index(command)
        # Change the command to be the long form
        command = directions[pos]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You Cannot Go This Way.")    
    else:
        print()
    if command == 'read':
        test_letter.read_letter()

    if command == 'collect':
        item_name = input("What item? ")
        found = False
        for item in current_node.item:
            if item.name.lower() == item_name.lower():
                inventory.append(item)
                print("Taken.")
                found = True

        if not found:
            print("I don't see it here.")

    if command == 'buy':
        food_name = input("What do you want to buy? ")
        found = False
        for item in current_node.item:
            if item.name.lower() == food_name.lower():
                inventory.append(item)
                print("You bought it.")
                found = True

        if not found:
            print("I don't see that.")

    if command == "inventory":
        you_inventory = inventory

    if command == 'go to them':
        print("He is holding an action figure. He says he is lost. Being the person you are, you just stare at him "
              "blankly until he walks away.")
        found = False
