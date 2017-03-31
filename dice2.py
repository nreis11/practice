import random

class Die(object):

    def __init__(self):
        self.side = 0

    def throw(self):
        self.side = random.randint(1,6)
        self.get_value()

    def get_value(self):
        return self.side

die_1 = Die()
for i in range(10):
    die_1.throw()
    die_value = die_1.get_value()
    print('The value of the die is', die_value)
