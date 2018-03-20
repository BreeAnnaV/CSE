class Item(object):
    def __init__(self, name):
        self.name = name


class Toy(Item):
    def __init__(self, name):
        super(Toy, self).__init__(name)

    def play(self):
        print("You play with the %s." % self.name)


test_toy = Toy('action figure')
test_toy.play()


class StuffedAnimal(Toy):
    def __init__(self, name):
        super(StuffedAnimal, self).__init__(name)

    def collect_animal(self):
        print("You take the %s." % self.name)


test_animal = StuffedAnimal('stuffed rabbit')
test_animal.collect_animal()


class ActionFigure(Toy):
    def __init__(self, name):
        super(ActionFigure, self).__init__(name)

    def collect_figure(self):
        print("You take the %s action figure." % self.name)


test_figure = ActionFigure('batman')
test_figure.collect_figure()


class JoyStick(Toy):
    def __init__(self, name):
        super(JoyStick, self).__init__(name)

    def collect_stick(self):
        print("You take the joystick. This may come in handy later.")


class Clothing(Item):
    def __init__(self, name, brand):
        super(Clothing, self).__init__(name)
        self.brand = brand

    def wear(self):
        print("You wear the %s." % self.name)


test_clothing = Clothing('shirt', 'guess')
test_clothing.wear()


class Shirt(Clothing):
    def __init__(self, name, brand):
        super(Shirt, self).__init__(name, brand)

    def collect_shirt(self):
        print("You take the %s shirt." % self.brand)


test_shirt = Shirt('shirt', 'supreme')
test_shirt.collect_shirt()
test_shirt.wear()


class Pants(Clothing):
    def __init__(self, name, brand):
        super(Pants, self).__init__(name, brand)

    def collect_pants(self):
        print("You take the %s pants." % self.brand)


test_pants = Pants('pants', 'gucci')
test_pants.wear()
test_pants.collect_pants()


class Shoes(Clothing):
    def __init__(self, name, brand):
        super(Shoes, self).__init__(name, brand)

    def collect_shoes(self):
        print("You take the %s %s." % (self.brand, self.name))


test_shoes = Shoes('slides', 'gucci')
test_shoes.collect_shoes()
test_shoes.wear()


class Hat(Clothing):
    def __init__(self, name, brand):
        super(Hat, self).__init__(name, brand)

    def collect_hat(self):
        print("You take the %s %s." % (self.brand, self.name))


test_hat = Hat('beanie', 'north face')
test_hat.collect_hat()
test_hat.wear()


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
