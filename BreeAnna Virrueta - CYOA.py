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


# test_toy = Toy('action figure')
# test_toy.play()


class StuffedAnimal(Toy):
    def __init__(self, name):
        super(StuffedAnimal, self).__init__(name)

    def collect_animal(self):
        print("You take the %s." % self.name)


# test_animal = StuffedAnimal('stuffed rabbit')
# test_animal.collect_animal()


class ActionFigure(Toy):
    def __init__(self, name):
        super(ActionFigure, self).__init__(name)

    def collect_figure(self):
        print("You take the %s action figure." % self.name)


# test_figure = ActionFigure('batman')
# test_figure.collect_figure()


class JoyStick(Toy):
    def __init__(self, name):
        super(JoyStick, self).__init__(name)

    def collect_joystick(self):
        print("You take the joystick. This may come in handy later.")


class Clothing(Item):
    def __init__(self, name, brand):
        super(Clothing, self).__init__(name)
        self.brand = brand

    def wear(self):
        print("You wear the %s." % self.name)


# test_clothing = Clothing('shirt', 'guess')
# test_clothing.wear()


class Shirt(Clothing):
    def __init__(self, name, brand):
        super(Shirt, self).__init__(name, brand)

    def collect_shirt(self):
        print("You take the %s shirt." % self.brand)


# test_shirt = Shirt('shirt', 'supreme')
# test_shirt.collect_shirt()
# test_shirt.wear()


class Pants(Clothing):
    def __init__(self, name, brand):
        super(Pants, self).__init__(name, brand)

    def collect_pants(self):
        print("You take the %s pants." % self.brand)


# test_pants = Pants('pants', 'gucci')
# test_pants.wear()
# test_pants.collect_pants()


class Shoes(Clothing):
    def __init__(self, name, brand):
        super(Shoes, self).__init__(name, brand)

    def collect_shoes(self):
        print("You take the %s %s." % (self.brand, self.name))


# test_shoes = Shoes('slides', 'gucci')
# test_shoes.collect_shoes()
# test_shoes.wear()


class Hat(Clothing):
    def __init__(self, name, brand):
        super(Hat, self).__init__(name, brand)

    def collect_hat(self):
        print("You take the %s %s." % (self.brand, self.name))


# test_hat = Hat('beanie', 'north face')
# test_hat.collect_hat()
# test_hat.wear()


class HockeyPuck(Item):
    def __init__(self, name):
        super(HockeyPuck, self).__init__(name)

    def collect_puck(self):
        print("You take the hockey puck. This may come in handy later.")


class MiniGolfBall(Item):
    def __init__(self, name):
        super(MiniGolfBall, self).__init__(name)

    def collect_ball(self):
        print("You take the mini golf ball. This may come in handy later.")


class CarKey(Item):
    def __init__(self, name):
        super(CarKey, self).__init__(name)

    def collect_key(self):
        print("You take the car key. This may come in handy later.")


class SteeringWheel(Item):
    def __init__(self, name):
        super(SteeringWheel, self).__init__(name)

    def collect_wheel(self):
        print("You take the steering wheel. This may come in handy later.")


class WelcomeLetter(Item):
    def __init__(self, name, words):
        super(WelcomeLetter, self).__init__(name)
        self.words = words

    def read_letter(self):
        print("You read the letter. %s" % self.words)


# test_letter = WelcomeLetter('Welcome Letter', 'Welcome to the game. The goal is to collect everything you can and '
#                                               'put it into a case you will have to find. If you do not find '
#                                               'everything, you will not be able to win the game. If you are able to '
#                                               'collect everything, you win the game. Along the way you will discover'
#                                               'many other fun activities to do. Good Luck.')
# test_letter.read_letter()


class Basketball(Item):
    def __init__(self, name):
        super(Basketball, self).__init__(name)

    def shoot_ball(self):
        print("You did not make it.")


class Weapon(Item):
    def __init__(self, name, durability):
        super(Weapon, self).__init__(name)
        self.durability = durability

    def attack(self):
        print("You hit something.")
        self.durability = ('%s' % self.durability)


test_weapon = Weapon('sword', '90%')


class Bat(Weapon):
    def __init__(self, name, durability):
        super(Bat, self).__init__(name, durability)

    def collect_bat(self):
        print("You take the bat with %s durability." % self.durability)


# test_bat = Bat('bat', '90%')
# test_bat.attack()
# test_bat.collect_bat()


class HockeyStick(Weapon):
    def __init__(self, name, durability):
        super(HockeyStick, self).__init__(name, durability)

    def collect_stick(self):
        print("You take the hockey stick with %s durability." % self.durability)


class Wrench(Weapon):
    def __init__(self, name, durability):
        super(Wrench, self).__init__(name, durability)

    def collect_wrench(self):
        print("You take the wrench with %s durability" % self.durability)


class Consumable(Item):
    def __init__(self, name, price):
        super(Consumable, self).__init__(name)
        self.price = price

    # def buy(self):
    #     print("The price is %s. Do you want to buy it?" % self.price)
    # command = input('>_')
    # if command == 'yes':
    #         print("It is all yours.")
    # elif command == 'no':
    #         print("You did not buy it.")


# test_consumable = Consumable('salad', '$50')
# test_consumable.buy()


class CornDog(Consumable):
    def __init__(self, name, price):
        super(CornDog, self).__init__(name, price)

    def eat_corndog(self):
        print("You eat the %s." % self.name)


class Soda(Consumable):
    def __init__(self, name, price):
        super(Soda, self).__init__(name, price)

    def drink_soda(self):
        print("You take a sip of the %s." % self.name)


# test_soda = Soda('sprite', '$2')
# test_soda.drink_soda()


class Salad(Consumable):
    def __init__(self, name, price):
        super(Salad, self).__init__(name, price)

    def eat_salad(self):
        print("You eat the %s." % self.name)


class Candy(Consumable):
    def __init__(self, name, price):
        super(Candy, self).__init__(name, price)

    def eat_candy(self):
        print("You eat the %s." % self.name)


# test_candy = Candy('skittles', '3 dollars')
# test_candy.buy()


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
            print("You move.")
        else:
            print("Nothing happens.")

    def move_forward(self, spaces):
        self.spaces = spaces
        self.move()
        print("You move forward %s spaces." % spaces)

    def spawn(self):
        print("You spawn in the world.")


# character = Characters("Joe", "Tall", "Has a sword and cherries", True, "100%")
# character.spawn()

class Room(object):
    def __init__(self, name, description, north, west, east, south, left, right, leave, item):
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

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


CENTER = Room("Center of the Mall", "You are outside a huge shopping center.", 'KIDS', 'FOOD', 'ARCADE', None, None,
              None, None, WelcomeLetter)
FOOD = Room("Food Court", "You are inside. You see many different restaurants.", 'CLOTHES', 'GOLF', 'CENTER',
            'RESTROOMS', None, None, None, Consumable)
RESTROOMS = Room("Restrooms", "There are two doors. One leading to the female room, the other to the male room. Go "
                              "left or right.", 'FOOD', None, None, None, 'MEN', 'WOMEN', None, None)
WOMEN = Room("Women Restroom", "There is nobody in here. There is a door leading south.", None, None, None, 'PARKING',
             None, None, 'RESTROOMS', None)
MEN = Room("Men Restroom", "You see someone in the corner. You could go up to them, or go south.", None, None, None,
           'PARKING', None, None, 'RESTROOMS', None)
PARKING = Room('Parking Garage', "You are outside, behind the mall. You see a door pretty far from you leading back "
                                 "inside.", 'RESTROOMS', 'GARAGE', 'BASKETBALL', None, None, None, None, CarKey)
GOLF = Room("Mini Golf Course", "You are in a slightly lit room with many people waiting in a line. You see golf balls "
                                "and clubs.", None, None, 'FOOD', 'GARBAGE', None, None, None, MiniGolfBall)
GARBAGE = Room("Dumpsters", "There is a terrible smell coming from the dumpsters.", 'GOLF', None, 'PARKING', None,
               None, None, None, SteeringWheel)
BASKETBALL = Room("Basketball Courts", "Basketballs are flying everywhere and you are trying your best not to get hit. "
                                       "Your only way out is through a door to the north.", 'SPORTS', 'PARKING', None,
                  None, None, None, None, Basketball)
SPORTS = Room("Sports Center", "There are multiple hallways in front of you.", 'ARCADE', 'BAT', 'ICE', 'BASKETBALL',
              None, None, None, None)
ICE = Room("Ice Rink", "All of a sudden it gets extremely cold. You could get skates, or just carry on with your life.",
           None, 'SPORTS', 'SWIM', None, None, None, None, (HockeyStick, HockeyPuck))
BAT = Room('Batting Cage', "You like baseball? You can practice your bating skills now.", None, None, 'SPORTS', None,
           None, None, None, Bat)
SWIM = Room("Swimming Pools", "The room is full of pools.", None, 'ICE', None, None, None, None, None, None)
CLOTHES = Room("Clothing Stores", "The stores are flooded with people, but it is your lucky day, you are already "
                                  "wearing clothes!", None, None, 'KIDS', 'FOOD', None, None, None, Clothing)
KIDS = Room("Kids Area", "You are outside. Kids are running around and you hear a huge crash. To the east you see "
                         "cars.", None, 'CLOTHES', 'RACE', 'CENTER', None, None, None, (ActionFigure, StuffedAnimal))
RACE = Room("Race Track", "A huge track is in front of you.", None, 'KIDS', None, None, None, None, None, Wrench)
ARCADE = Room("Arcade", "A room full of retro machines and new gadgets.", None, 'CENTER', None, 'SPORTS', None, None,
              None, JoyStick)


center_node = Room("Center of the Mall", "You are outside a huge shopping center.", 'KIDS', 'FOOD', 'ARCADE', None,
                   None, None, None, WelcomeLetter)


current_node = center_node
directions = ['north', 'west', 'east', 'south', 'left', 'right', 'leave']
short_directions = ['n', 'w', 'e', 's']

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
        print("Command Not Recognized.")
    print()
