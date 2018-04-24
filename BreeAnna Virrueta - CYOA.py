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


class StuffedRabbit(Toy):
    def __init__(self):
        super(StuffedRabbit, self).__init__(name="Stuffed Rabbit")

    def collect_animal(self):
        print("You take the %s." % self.name)


# test_animal = StuffedRabbit()
# test_animal.collect_animal()


class ActionFigure(Toy):
    def __init__(self):
        super(ActionFigure, self).__init__(name="Batman")

    def collect_figure(self):
        print("You take the %s action figure." % self.name)


# test_figure = ActionFigure()
# test_figure.collect_figure()


class JoyStick(Toy):
    def __init__(self):
        super(JoyStick, self).__init__(name="joystick")

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
    def __init__(self):
        super(HockeyPuck, self).__init__(name="hockey puck")

    def collect_puck(self):
        print("You take the hockey puck. This may come in handy later.")


class MiniGolfBall(Item):
    def __init__(self):
        super(MiniGolfBall, self).__init__(name="mini golf ball")

    def collect_ball(self):
        print("You take the mini golf ball. This may come in handy later.")


class CarKey(Item):
    def __init__(self):
        super(CarKey, self).__init__(name="car key")

    def collect_key(self):
        print("You take the car key. This may come in handy later.")


class SteeringWheel(Item):
    def __init__(self, name):
        super(SteeringWheel, self).__init__(name="steering wheel")

    def collect_wheel(self):
        print("You take the steering wheel. This may come in handy later.")


class WelcomeLetter(Item):
    def __init__(self, words):
        super(WelcomeLetter, self).__init__(name="Welcome Letter")
        self.words = words

    def read_letter(self):
        print("You read the letter. %s" % self.words)


# test_letter = WelcomeLetter('Welcome Letter', 'Welcome to the game. The goal is to collect everything you can and '
#                                               'put it into a case you at the Center of the Mall. If you do not find '
#                                               'everything, you will not be able to win the game. If you are able to '
#                                               'collect everything, you win the game. Along the way you will discover'
#                                               'many other fun activities to do. Good Luck.')
# test_letter.read_letter()


class Basketball(Item):
    def __init__(self):
        super(Basketball, self).__init__(name="basketball")

    def throw_ball(self):
        print("You hit someone. Run!")


class Weapon(Item):
    def __init__(self, name, durability):
        super(Weapon, self).__init__(name)
        self.durability = durability

    def attack(self):
        print("You hit something.")
        self.durability = ('%s' % self.durability)


test_weapon = Weapon('sword', '90%')


class Bat(Weapon):
    def __init__(self):
        super(Bat, self).__init__(name="bat",
                                  durability=100)

    def collect_bat(self):
        print("You take the bat with %s durability." % self.durability)


# test_bat = Bat()
# test_bat.collect_bat()
# test_bat.attack()


class HockeyStick(Weapon):
    def __init__(self, name, durability):
        super(HockeyStick, self).__init__(name="hockey stick",
                                          durability=100)

    def collect_stick(self):
        print("You take the hockey stick with %s durability." % self.durability)


class Wrench(Weapon):
    def __init__(self):
        super(Wrench, self).__init__(name="wrench",
                                     durability=100)

    def collect_wrench(self):
        print("You take the wrench with %s durability" % self.durability)


class Consumable(Item):
    def __init__(self, name, price):
        super(Consumable, self).__init__(name)
        self.price = price

    def buy(self):
        print("The price is %s. Do you want to buy it?" % self.price)
    command = input('>_')
    if command == 'yes':
            print("It is all yours.")
    elif command == 'no':
            print("You did not buy it.")


# test_consumable = Consumable('salad', '$50')
# test_consumable.buy()


class CornDog(Consumable):
    def __init__(self, name, price):
        super(CornDog, self).__init__(name="corn dog",
                                      price=2)

    def eat_corndog(self):
        print("You eat the %s." % self.name)


test_dog = CornDog('corn dog', 2)
test_dog.buy()
test_dog.eat_corndog()




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


boy_men = Characters("The little boy", "He is holding something.", ActionFigure, False)
you = Characters("You", None, 'Nothing', True)


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


CENTER = Room("Center of the Mall", "You are outside a huge shopping center.", 'KIDS', 'FOOD', 'ARCADE', None, None,
              None, None, WelcomeLetter, None)
FOOD = Room("Food Court", "You are inside. You see many different restaurants. Order a corn dog, soda, salad, or "
                          "candy.", 'CLOTHES', 'GOLF', 'CENTER', 'RESTROOMS', None, None, None, Consumable, None)
RESTROOMS = Room("Restrooms", "There are two doors. One leading to the female room, the other to the male room. Go "
                              "left or right.", 'FOOD', None, None, None, 'MEN', 'WOMEN', None, None, None)
WOMEN = Room("Women Restroom", "There is nobody in here. There is a door leading south.", None, None, None, 'PARKING',
             None, None, 'RESTROOMS', None, None)
MEN = Room("Men Restroom", "You see someone in the corner. You could go up to them, or go south.", None, None, None,
           'PARKING', None, None, 'RESTROOMS', None, boy_men)
PARKING = Room('Parking Garage', "You are outside, behind the mall. There is sometbing shiny on the ground. "
                                 "You see a door pretty far from you leading back inside.", 'RESTROOMS', 'GARAGE',
               'BASKETBALL', None, None, None, None, CarKey, None)
GOLF = Room("Mini Golf Course", "You are in a slightly lit room with many people waiting in a line. You see golf balls "
                                "and clubs.", None, None, 'FOOD', 'GARBAGE', None, None, None, MiniGolfBall, None)
GARBAGE = Room("Dumpsters", "There is a terrible smell coming from the dumpsters. You see something that catches your "
                            "attention.", 'GOLF', None, 'PARKING', None, None, None, None, SteeringWheel, None)
BASKETBALL = Room("Basketball Courts", "Basketballs are flying everywhere and you are trying your best not to get hit."
                                       "If you get one you can throw it at someone, or your only way out is through a "
                                       "door to the north.", 'SPORTS', 'PARKING', None, None, None, None, None,
                  Basketball, None)
SPORTS = Room("Sports Center", "There are multiple hallways in front of you.", 'ARCADE', 'BAT', 'ICE', 'BASKETBALL',
              None, None, None, None, None)
ICE = Room("Ice Rink", "All of a sudden it gets extremely cold. People are playing hockey on the ice. There is a puck "
                       "next to you, along with a stick", None, 'SPORTS', 'SWIM', None, None, None, None, (HockeyStick,
                                                                                                           HockeyPuck),
           None)
BAT = Room('Batting Cage', "You have been looking for a new bat. There is one in front of you.", None, None, 'SPORTS',
           None, None, None, None, Bat, None)
SWIM = Room("Swimming Pools", "The room is full of pools.", None, 'ICE', None, None, None, None, None, None, None)
CLOTHES = Room("Clothing Stores", "The stores are flooded with people, but it is your lucky day, you are already "
                                  "wearing clothes!", None, None, 'KIDS', 'FOOD', None, None, None, Clothing, None)
KIDS = Room("Kids Area", "You are outside. Kids are running around and you hear a huge crash. To the east you see "
                         "cars.", None, 'CLOTHES', 'RACE', 'CENTER', None, None, None, StuffedRabbit, None)
RACE = Room("Race Track", "A huge track is in front of you.You should take the wrench on the ground", None, 'KIDS',
            None, None, None, None, None, Wrench, None)
ARCADE = Room("Arcade", "A room full of retro machines and new gadgets.", None, 'CENTER', None, 'SPORTS', None, None,
              None, JoyStick, None)


center_node = Room("Center of the Mall", "You are outside a huge shopping center.", 'KIDS', 'FOOD', 'ARCADE', None,
                   None, None, None, WelcomeLetter, you)


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
