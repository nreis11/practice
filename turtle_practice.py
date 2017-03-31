# The turtle begins in the center of the screen.
# Flip a coin. If its heads then turn to the left 90 degrees.
# If its tails then turn to the right 90 degrees.
# Take 50 steps forward.
# If the turtle has moved outside the screen then stop,
# otherwise go back to step 2 and repeat.

import turtle
import random

def in_bounds(t):

    turtlex = t.xcor()                      #coordinates for turtle
    turtley = t.ycor()

    still_in = True                          # determine true/false for
    if int(turtlex) not in range(-300, 300):      # bounds of turtle
        still_in = False
    if int(turtley) not in range(-300, 300):
        still_in = False
    return still_in

def flip_a_coin(t):
        coin = random.randint(0,2)            # turtle doing random turns
        if coin == 0:
            t.lt(90)
        else:
            t.rt(90)
        t.fd(50) # turtle moving forward

def main():
    wn = turtle.Screen()
    wn.bgcolor('black')
    blu = turtle.Turtle()
    blu.showturtle()
    # blu.setpos(0, 0)
    blu.color('green')
    blu.pensize(2)
    blu.pendown()
    wn.setup(600, 600, startx=None, starty=None)
    while in_bounds(blu):
        flip_a_coin(blu)
    wn.exitonclick()
main()
