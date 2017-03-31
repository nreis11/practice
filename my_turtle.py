import turtle
import random, time

# Idea = Make a maze. Player can't touch edges.

# Set up screen
width = 800
height = 800
wn = turtle.Screen()
wn.bgcolor('black')
wn.setup(width, height, startx=None, starty=None)

# Draw border
# mypen = turtle.Turtle()
# mypen.color('blue')
# mypen.penup()
# mypen.setposition(-400, -400)
# mypen.pendown()
# mypen.pensize(3)
# for side in range(4):
#     mypen.forward(800)
#     mypen.left(90)
# mypen.hideturtle()

# Create player turtle
player = turtle.Turtle()
player.color('green')
player.shape('arrow')
player.speed(0)
player_speed = 1

# Define player functions
def turnleft():
    player.left(90)

def turnright():
    player.right(90)

def increasespeed():
    global player_speed
    player_speed += 1

def decreasespeed():
    global player_speed
    if player_speed < 1:
        player_speed = 1
    else:
        player_speed -= 1

# Set keyboard bindings
turtle.listen()
turtle.onkey(turnleft, 'Left')
turtle.onkey(turnright, 'Right')
turtle.onkey(increasespeed, 'Up')
turtle.onkey(decreasespeed, 'Down')




def random_xy(width, height):
    x = random.randint(-width / 2, width / 2)
    y = random.randint(-height / 2, height / 2)
    return (x, y)

def ai_heading():
    directions = range(0, 359, 90)
    return random.choice(directions)

def ai_turnleft():
    ai.left(90)

def ai_turnright():
    ai.right(90)

def ai_wait():
    return random.randint(0, 3000)

def ai_change_speed():
    global ai_speed
    ai_speed = random.randint(ai_speed - 2, ai_speed + 2)



# Create ai
ai = turtle.Turtle()
x, y = random_xy(width, height)
ai.setposition(x, y)
ai.color('red')
ai.shape('turtle')
ai.penup()
ai.setheading(ai_heading())
ai_speed = 2

while True:

    ai.forward(ai_speed)
    # turtle.ontimer(ai_turnleft(), ai_wait())
    # turtle.ontimer(ai_change_speed(), ai_wait())

    player.forward(player_speed)

    # Boundary check
    if player.xcor() > 400 or player.xcor() < -400:
        player.penup()
        player.clear()
        player.setposition(0,0)
        player.pendown()
    if player.ycor() > 400 or player.ycor() < -400:
        player.penup()
        player.clear()
        player.setposition(0,0)
        player.pendown()






















delay = input('Press Enter to finish')
