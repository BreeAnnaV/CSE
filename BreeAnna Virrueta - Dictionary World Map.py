world_map = {
    'CENTER': {
        'NAME': "Center of the Mall",
        'DESCRIPTION': "You are outside a huge shopping center.",
        'PATHS': {
            'NORTH': 'KIDS',
            'WEST': 'FOOD',
            'EAST': 'ARCADE'
        }
    },
    'FOOD': {
        'NAME': 'Food Court',
        'DESCRIPTION': "You are inside. You see many different restaurants.",
        'PATHS': {
            'EAST': 'CENTER',
            'NORTH': 'CLOTHES',
            'WEST': 'GOLF',
            'SOUTH': 'RESTROOMS'
        }
    },
    'RESTROOMS': {
        'NAME': 'Restrooms',
        'DESCRIPTION': 'There are two doors. One leading to the female room, the other to the male room. Go left or '
                       'right.',
        'PATHS': {
            'RIGHT': 'WOMEN',
            'LEFT': 'MEN',
            'NORTH': 'FOOD'
        }
    },
    'WOMEN': {
        'NAME': 'Women Restroom',
        'DESCRIPTION': 'There is nobody in here. There is a door leading south.',
        'PATHS': {
            'LEAVE': 'RESTROOM',
            'SOUTH': 'PARKING'
        }

    },
    'MEN': {
        'NAME': 'Men Restroom',
        'DESCRIPTION': 'You see someone in the corner. You could go up to them, or go south.',
        'PATHS': {
            'LEAVE': 'RESTROOM',
            'SOUTH': 'PARKING'
        }
    },
    'PARKING': {
        'NAME': 'Parking Garage',
        'DESCRIPTION': 'You are outside, behind the mall. You see a door pretty far from you leading back inside.',
        'PATHS': {
            'NORTH': 'RESTROOMS',
            'WEST': 'GARBAGE',
            'EAST': 'BASKETBALL',
        }
    },
    'GOLF': {
        'NAME': 'Mini Golf Course',
        'DESCRIPTION': 'You are in a slightly lit room with many people waiting in a line. You see golf balls and clubs'
                       '. Do you want to play a round, or leave?',
        'PATHS': {
            'EAST': 'FOOD',
            'SOUTH': 'GARBAGE'
        }
    },
    'GARBAGE': {
        'NAME': 'Dumpsters',
        'DESCRIPTION': 'There is a terrible smell coming from the dumpsters.',
        'PATHS': {
            'EAST': 'PARKING',
            'NORTH': 'GOLF'
        }
    },
    'BASKETBALL': {
        'NAME': 'Basketball Courts',
        'DESCRIPTION': 'Basketballs are flying everywhere and you are trying your best not to get hit. Your only way '
                       'out is through a door to the north.',
        'PATHS': {
            'NORTH': 'SPORTS',
            'WEST': 'PARKING'
        }
    },
    'SPORTS': {
        'NAME': 'Sports Center',
        'DESCRIPTION': 'There are multiple hallways in front of you.',
        'PATHS': {
            'WEST': 'BAT',
            'EAST': 'ICE',
            'SOUTH': 'BASKETBALL',
            'NORTH': 'ARCADE'
        }
    },
    'ICE': {
        'NAME': 'Ice Rink',
        'DESCRIPTION': 'All of a sudden it gets extremely cold. You could get skates, or just carry on with your life.',
        'PATHS': {
            'EAST': 'SWIM',
            'WEST': 'SPORTS'
        }
    },
    'BAT': {
        'NAME': 'Batting Cage',
        'DESCRIPTION': 'You like baseball? You can practice your bating skills now.',
        'PATHS': {
            'EAST': 'SPORTS'
        }
    },
    'SWIM': {
        'NAME': 'Swimming Pools',
        'DESCRIPTION': 'The room is full of pools.',
        'PATHS': {
            'WEST': 'ICE'
        }
    },
    'CLOTHES': {
        'NAME': 'Clothing Stores',
        'DESCRIPTION': 'The stores are flooded with people, but it is your lucky day, you are already wearing clothes!',
        'PATHS': {
            'SOUTH': 'FOOD',
            'EAST': 'KIDS'
        }
    },
    'KIDS': {
        'NAME': 'Kids Area',
        'DESCRIPTION': 'You are outside. Kids are running around and you hear a huge crash. To the east you see cars.',
        'PATHS': {
            'WEST': 'CLOTHES',
            'SOUTH': 'CENTER',
            'EAST': 'RACE'
        }
    },
    'RACE': {
        'NAME': 'Race Track',
        'DESCRIPTION': 'A huge track is in front of you.',
        'PATHS': {
            'WEST': 'KIDS'
        }
    },
    'ARCADE': {
        'NAME': 'Arcade',
        'DESCRIPTION': 'A room full of retro machines and new gadgets.',
        'PATHS': {
            'SOUTH': 'SPORTS',
            'WEST': 'CENTER'
        }
    }
}

current_node = world_map['CENTER']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'RIGHT', 'LEFT', 'LEAVE']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print("You cannot go this way.")
    else:
        print("Command not Recognized.")
    print()
