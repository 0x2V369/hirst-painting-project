import colorgram
import turtle
from random import choice

# Constants for the painting
DOT_SIZE = 20
SPACING = 50
GRID_SIZE = 10

# Extract colors from an image
colors = colorgram.extract('image.jpg', 25)
color_list = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

# Turtle setup
t = turtle.Turtle()
turtle.colormode(255)
# t.speed('fastest')
t.hideturtle()


def draw_dot():
    """
    Draw a single dot with a random color.
    """
    random_color = choice(color_list)
    t.dot(DOT_SIZE, random_color)


def move_one_row_up():
    """
    Move the turtle to the beginning of the next row.
    """
    t.setheading(90)
    t.forward(SPACING)
    t.setheading(180)
    t.forward(GRID_SIZE * SPACING)
    t.setheading(0)


def paint_art():
    """
    Draw a grid of dots to create the painting.
    """
    for _ in range(GRID_SIZE):
        for _ in range(GRID_SIZE):
            draw_dot()
            t.penup()
            t.forward(SPACING)
        move_one_row_up()


# Setup screen
screen = turtle.Screen()
screen.setup(640, 640)
screen.setworldcoordinates(-20, -20, screen.window_width() - 20, screen.window_height() - 20)

# Start painting
paint_art()

screen.exitonclick()
