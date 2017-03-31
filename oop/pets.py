class Pet(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        raise NotImplementedError('Subclass must implement abstract method')

class Cat(Pet):

    def __init__(self, name, age):
        super().__init__(name, age) # to run super class methods

    def talk(self):
        return "Meow"

class Dog(Pet):

    def __init__(self, name, age):
        super().__init__(name, age)

    def talk(self):
        return "Wooof!"

def Main():

    thePet = Pet('Pet', 1)
    jess = Cat('Jess', 3)

    print('Is Jess a Cat?' + str(isinstance(jess, Cat)))
    print('Is Jess a Pet?' + str(isinstance(jess, Pet)))
    print('Is thePet a Cat?' + str(isinstance(thePet, Cat)))
    print('Is thePet a Pet?' + str(isinstance(thePet, Pet)))

    pets = [Cat('Jess', 3), Dog('Jack', 2), Cat('Fred', 1), Pet('thePet', 5)]

    for pet in pets:
        print('Name: {}, Age: {} says: {}'.format(pet.name, pet.age, pet.talk()))

if __name__ == '__main__':
    Main()
