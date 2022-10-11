"""
main script of the turtlekit module.
"""
# importing
from turtle import Turtle, Screen


def get_screen():
    """
    A function that returns a screen. Takes no parameters.
    """
    screen = Screen()
    return screen


def draw_square(sidelength:int, start_angle:int, start_at:tuple, color, infill=True, pensize = 5):
    """
    Draws a square with the specifed sidelength, and infills if needed. Always starts from left-hand corner of square.

    #### Parameters

    `sidelength` : The side length that the square should be, in integer format.

    `start_angle` : The angle that the square should rotated by when drawing, as an integer. Always rotates left.

    `start_at` : A tuple with the x and y coordinates of where the shape should be drawn.

    `color` : The color the shape should be when drawn.

    `infill` : An optional boolean value taht indicates if the shape should be filled. Defaults to True.

    `pensize` : Optional value indicating the pensize of the turtle. Defaults to 5.
    """
    # defining turtle characteristics
    turt = Turtle()
    turt.hideturtle()
    turt.speed(0)
    turt.pensize(pensize)
    turt.color(color)
    turt.penup()
    turt.goto(start_at)
    turt.left(start_angle)
    turt.pendown()
    # drawing shape
    if infill is True:
        turt.fillcolor(color)
        turt.begin_fill()
        for i in range(4):
            turt.forward(sidelength)
            turt.left(90)
        turt.end_fill()
    else:
        for i in range(4):
            turt.forward(sidelength)
            turt.left(90)


def draw_rectangle(width:int, length:int, start_angle:int, start_at:tuple, color, infill=True, pensize = 5):
    """
    Draws a rectangle with the specifed width and length, and infills if needed. Always starts from left-hand corner of square.

    #### Parameters

    `width` : The width that the rectangle should be, in integer format.

    `length` : The length that the rectangle should be, in integer format.

    `start_angle` : The angle that the rectangle should rotated by when drawing, as an integer. Always rotates left.

    `start_at` : A tuple with the x and y coordinates of where the rectangle should be drawn.

    `color` : The color the rectangle should be when drawn.

    `infill` : An optional boolean value that indicates if the rectangle should be filled. Defaults to True.

    `pensize` : Optional value indicating the pensize of the turtle. Defaults to 5.
    """
    # defining turtle characteristics
    turt = Turtle()
    turt.hideturtle()
    turt.speed(0)
    turt.pensize(pensize)
    turt.color(color)
    turt.penup()
    # going to start pos and setting to angle
    turt.goto(start_at)
    turt.left(start_angle)
    turt.pendown()
    # drawing shape, infilling if needed
    if infill is True:
        turt.fillcolor(color)
        turt.begin_fill()
        for i in range(2):
            turt.forward(width)
            turt.left(90)
            turt.forward(length)
            if i == 0:
                turt.left(90)
        turt.end_fill()
    else:
        for i in range(2):
            turt.forward(width)
            turt.left(90)
            turt.forward(width)
            if i == 0:
                turt.left(90)
    del turt


def draw_equilateral_triangle(side_length:int, start_angle:int, start_at:tuple, color, infill = True, pensize = 5):
    """
    Draws an equilateral triangle with the specifed sidelength, and infills if needed. Always starts from left-hand corner of square.

    #### Parameters

    `side_length` : The side length that the triangle should be, in integer format.

    `start_angle` : The angle that the triangle should rotated by when drawing, as an integer. Always rotates left.

    `start_at` : A tuple with the x and y coordinates of where the triangle should be drawn.

    `color` : The color the triangle should be when drawn.

    `infill` : An optional boolean value that indicates if the triangle should be filled. Defaults to True.

    `pensize` : Optional value indicating the pensize of the turtle. Defaults to 5.
    """
    # defining turtle characteristics
    turt = Turtle()
    turt.hideturtle()
    turt.speed(0)
    turt.pensize(pensize)
    turt.color(color)
    turt.penup()
    # going to start pos and setting to angle
    turt.goto(start_at)
    turt.left(start_angle)
    turt.pendown()
    if infill is True:
        turt.fillcolor(color)
        turt.begin_fill()
        for i in range(3):
            turt.forward(side_length)
            turt.left(120)
        turt.end_fill()
    else:
        for i in range(3):
            turt.forward(side_length)
            turt.left(120)
    del turt
    pass


def draw_octagon(side_length:int, start_angle:int, start_at:tuple, color, infill=True, pensize = 5):
    """
    Draws an octagon with the specifed sidelength, and infills if needed. Always starts from left-hand corner of square.

    #### Parameters

    `sidelength` : The side length that the octagon should be, in integer format.

    `start_angle` : The angle that the octagon should rotated by when drawing, as an integer. Always rotates left.

    `start_at` : A tuple with the x and y coordinates of where the octagon should be drawn.

    `color` : The color the octagon should be when drawn.

    `infill` : An optional boolean value that indicates if the octagon should be filled. Defaults to True.

    `pensize` : Optional value indicating the pensize of the turtle. Defaults to 5.
    """
    # setting turtle + attributes
    turt = Turtle()
    turt.hideturtle()
    turt.speed(0)
    turt.pensize(pensize)
    turt.color(color)
    turt.penup()
    turt.goto(start_at)
    turt.left(start_angle)
    turt.pendown()
    # drawing outline
    if infill is True:
        turt.fillcolor(color)
        turt.begin_fill()
        for i in range(8):
            turt.forward(side_length)
            turt.left(45)
        turt.end_fill()
    else:
        for i in range(8):
            turt.forward(side_length)
            turt.left(45)


def draw_hexagon(side_length:int, start_angle:int, start_at:tuple, color, infill=True, pensize = 5):
    """
    Draws an hexagon with the specifed sidelength, and infills if needed. Always starts from left-hand corner of square.

    #### Parameters

    `sidelength` : The side length that the hexagon should be, in integer format.

    `start_angle` : The angle that the hexagon should rotated by when drawing, as an integer. Always rotates left.

    `start_at` : A tuple with the x and y coordinates of where the hexagon should be drawn.

    `color` : The color the hexagon should be when drawn.

    `infill` : An optional boolean value that indicates if the hexagon should be filled. Defaults to True.

    `pensize` : Optional value indicating the pensize of the turtle. Defaults to 5.
    """
    # setting turtle + attributes
    turt = Turtle()
    turt.hideturtle()
    turt.speed(0)
    turt.pensize(pensize)
    turt.color(color)
    turt.penup()
    turt.goto(start_at)
    turt.left(start_angle)
    turt.pendown()
    # drawing outline
    if infill is True:
        turt.fillcolor(color)
        turt.begin_fill()
        for i in range(6):
            turt.forward(side_length)
            turt.left(60)
        turt.end_fill()
    else:
        for i in range(6):
            turt.forward(side_length)
            turt.left(60)


def draw_n_side_shape(num_sides:int, side_length:int, start_angle:int, start_at:tuple, color, infill=True, pensize=5):
    """
    Draws a shape with `n` sides and the specifed sidelength, and infills if needed. Always starts from bottom-left of shape.

    #### Parameters

    `num_sides` : The number of sides the shape should have.

    `sidelength` : The side length that the shape should be, in integer format.

    `start_angle` : The angle that the shape should rotated by when drawing, as an integer. Always rotates left.

    `start_at` : A tuple with the x and y coordinates of where the shape should be drawn.

    `color` : The color the shape should be when drawn.

    `infill` : An optional boolean value that indicates if the shape should be filled. Defaults to True.

    `pensize` : Optional value indicating the pensize of the turtle. Defaults to 5.
    """
    # calculating inner angles
    angle = 360/num_sides
    # setting turtle + attributes
    turt = Turtle()
    turt.hideturtle()
    turt.speed(0)
    turt.pensize(pensize)
    turt.color(color)
    turt.penup()
    turt.goto(start_at)
    turt.left(start_angle)
    turt.pendown()
    # drawing outline
    if infill is True:
        turt.fillcolor(color)
        turt.begin_fill()
        for i in range(num_sides):
            turt.forward(side_length)
            turt.left(angle)
        turt.end_fill()
    else:
        for i in range(num_sides):
            turt.forward(side_length)
            turt.left(angle)


screen = get_screen()
screen.bgcolor("Purple")
screen.colormode(255)
draw_rectangle(120, 60, 0, (0, 0), "Red", infill=False)
screen.exitonclick()