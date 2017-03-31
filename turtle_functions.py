import turtle

window = turtle.Screen()
window.bgcolor('black')

# Define constants
# Use capital letters
TRIANGLE = 3
SQUARE = 4
PENTAGON = 5
HEXAGON = 6
HEPTAGON = 7

def draw_shape(sides, color):
    turtle.color(color)
    turtle.pendown()
    for i in range(sides):
        turtle.fd(50)
        turtle.lt(360/sides)
    turtle.penup()
    turtle.fd(75)

turtle.penup()
turtle.goto(-250, 0)

draw_shape(TRIANGLE, 'blue')
draw_shape(SQUARE, 'red')
draw_shape(PENTAGON, 'green')
draw_shape(HEXAGON, 'white')
draw_shape(HEPTAGON, 'orange')


delay = input('Press enter to exit')
