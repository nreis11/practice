class BaseCharacter(object):

    def __init__(self, name):
        self.name = name
        self.health = 100

    def print_name(self):
        print self.name

class NPC(BaseCharacter):

    playable = False

    def __init__(self, name):
        self.name = name

class Friendly(NPC):

    friend = True

    def __init__(self, name):
        self.name = name

class Enemy(NPC):

    enemy = True

    def __init__(self, name):
        self.attack_damage = 5
        self.name = name

class PC(BaseCharacter):

    playable = True

    def __init__(self, name, experience = 0):
        super(PC, self).__init__(name)
        self.experience = experience

class Archer(PC):

    def __init__(self,name):
        super(Archer, self).__init__(name)
        self.arrows = 10

class Warrior(PC):

    def __init__(self,name):
        super(Warrior, self).__init__(name)
        self.sword = 1
        self.shield = 0



Lucas = NPC('Lucas')
Judas = Enemy('Judas')
Link = PC('Link')
Legalos = Archer('Legalos')
Aragorn = Warrior('Aragorn')
