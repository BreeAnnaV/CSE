class Room(object):
    def __init__(self, name, description, north, west, east, south, left, right, leave):
        self.name = name
        self.description = description
        self.north = north
        self.west = west
        self.east = east
        self.south = south
        self.left = left
        self.right = right
        self.leave = leave

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]

center_mall = CENTER

current_node = center_mall
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
                name_of_node = current_node.name[command]
                current_node = [name_of_node]
            except KeyError:
                print("You Cannot Go This Way.")
        else:
            print("Command Not Recognized.")
        print()


CENTER = Room("Center of the Mall", "You are outside a huge shopping center.", 'KIDS', 'FOOD', 'ARCADE', None, None,
              None, None)
FOOD = Room("Food Court", "You are inside. You see many different restaurants.", 'CLOTHES', 'GOLF', 'CENTER',
            'RESTROOMS', None, None, None)
RESTROOMS = Room("Restrooms", "There are two doors. One leading to the female room, the other to the male room. Go left"
                              " or right."'FOOD', None, None, None, 'MEN', 'WOMEN', None, None)
WOMEN = Room("Women Restroom", "There is nobody in here. There is a door leading south.", None, None, None, 'PARKING',
             None, None, 'RESTROOM')
MEN = Room("Men Restroom", "You see someone in the corner. You could go up to them, or go south.", None, None, None,
           'PARKING', None, None, 'RESTROOM')
PARKING = Room('Parking Garage', "You are outside, behind the mall. You see a door pretty far from you leading back "
                                 "inside.", 'RESTROOMS', 'GARAGE', 'BASKETBALL', None, None, None, None, )
GOLF = Room("Mini Golf Course", "You are in a slightly lit room with many people waiting in a line. You see golf balls "
                                "and clubs. Do you want to play a round, or leave?", None, None, 'FOOD', 'GARBAGE',
            None, None, None)
GARBAGE = Room("Dumpsters", "There is a terrible smell coming from the dumpsters.", 'GOLF', None, 'PARKING', None,
               None, None, None)
BASKETBALL = Room("Basketball Courts", "Basketballs are flying everywhere and you are trying your best not to get hit. "
                                       "Your only way out is through a door to the north.", 'SPORTS', 'PARKING', None,
                  None, None, None, None)
SPORTS = Room("Sports Center", "There are multiple hallways in front of you.", 'ARCADE', 'BAT', 'ICE', 'BASKETBALL',
              None, None, None)
ICE = Room("Ice Rink", "All of a sudden it gets extremely cold. You could get skates, or just carry on with your life.",
           None, 'SPORTS', 'SWIM', None, None, None, None)
BAT = Room('Batting Cage', "You like baseball? You can practice your bating skills now.", None, None, 'SPORTS', None,
           None, None, None)
SWIM = Room("Swimming Pools", "The room is full of pools.", None, 'ICE', None, None, None, None, None)
CLOTHES = Room("Clothing Stores", "The stores are flooded with people, but it is you lucky day, you are already "
                                  "wearing clothes!", None, None, 'KIDS', 'FOOD', None, None, None)
KIDS = Room("Kids Area", "You are outside. Kids are running around and you hear a huge crash. To the east you see "
                         "cars.", None, 'CLOTHES', 'RACE', 'CENTER', None, None, None)
RACE = Room("Race Track", "'A huge track is in front of you.", None, 'KIDS', None, None, None, None, None)
ARCADE = Room("Arcade", "A room full of retro machines and new gadgets.", None, 'CENTER', None, 'SPORTS', None, None,
              None)
