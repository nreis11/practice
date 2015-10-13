import random

print "Welcome to the dice rolling game."

min = 1
max = 6
roll_again = 'yes' or 'y'

while roll_again == 'yes' or roll_again == 'y':
    print "The values you rolled are: "
    print random.randint(min, max)
    print random.randint(min, max)

    roll_again = raw_input("Roll again? ")
