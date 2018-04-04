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

    current_node = room_center
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
