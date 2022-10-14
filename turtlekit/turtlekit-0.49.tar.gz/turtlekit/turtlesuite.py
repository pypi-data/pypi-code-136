from turtle import Turtle, Screen


def get_screen():
    """
    Returns a Screen object.
    """
    screen = Screen()
    return screen


def draw_square(side_length:int, start_angle:int, start_at:tuple, color, infill=True, pensize=5):
    """
    A function that draws a square to an existing Screen.

    #### Parameters

    `side_length` : How long the sides of the square should be.

    `start_angle` : what angle to tilt the square at. Rotates left.

    `start_at` : The x/y coordinates of the point to start at.

    `color` : the color and infill color of the square, if applicable.

    `infill` : parameter that toggles infilling of shapes.

    `pensize` : The size of the pen to draw with.
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
    if infill is True:
        turt.fillcolor(color)
        turt.begin_fill()
        for i in range(4):
            turt.forward(side_length)
            turt.left(90)
        turt.end_fill()
    else:
        for i in range(4):
            turt.forward(side_length)
            turt.left


def draw_rectangle(width:int, length:int, start_angle:int, start_at:tuple, color, infill=True, pensize=5):
    """
    A function that draws a square to an existing Screen.

    #### Parameters

    `side_length` : How long the sides of the square should be.

    `start_angle` : what angle to tilt the square at. Rotates left.

    `start_at` : The x/y coordinates of the point to start at.

    `color` : the color and infill color of the square, if applicable.

    `infill` : parameter that toggles infilling of shapes.

    `pensize` : The size of the pen to draw with.
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
            turt.forward(length)
            if i == 0:
                turt.left(90)



def draw_equilateral_triangle(side_length:int, start_angle:int, start_at:tuple, color, infill=True, pensize=5):
    """
    A function that draws an equilateral triangle to an existing Screen.

    #### Parameters

    `side_length` : How long the sides of the equilateral triangle should be.

    `start_angle` : what angle to tilt the equilateral triangle at. Rotates left.

    `start_at` : The x/y coordinates of the point to start at.

    `color` : the color and infill color of the equilateral triangle, if applicable.

    `infill` : parameter that toggles infilling of shapes.

    `pensize` : The size of the pen to draw with.
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


def draw_octagon(side_length:int, start_angle:int, start_at:tuple, color, infill=True, pensize=5):
    """
    A function that draws an octagon to an existing Screen.

    #### Parameters

    `side_length` : How long the sides of the octagon should be.

    `start_angle` : what angle to tilt the octagon at. Rotates left.

    `start_at` : The x/y coordinates of the point to start at.

    `color` : the color and infill color of the octagon, if applicable.

    `infill` : parameter that toggles infilling of shapes.

    `pensize` : The size of the pen to draw with.
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


def draw_hexagon(side_length:int, start_angle:int, start_at:tuple, color, infill=True, pensize=5):
    """
    A function that draws a hexagon to an existing Screen.

    #### Parameters

    `side_length` : How long the sides of the hexagon should be.

    `start_angle` : what angle to tilt the hexagon at. Rotates left.

    `start_at` : The x/y coordinates of the point to start at.

    `color` : the color and infill color of the hexagon, if applicable.

    `infill` : parameter that toggles infilling of shapes.

    `pensize` : The size of the pen to draw with.
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
    # drawing shape
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
    A function that draws a shape with `n` sides to an existing Screen.

    #### Parameters

    `num_sides` : The number of sides the shape should have.

    `side_length` : How long the sides of the shape should be.

    `start_angle` : what angle to tilt the shape at. Rotates left.

    `start_at` : The x/y coordinates of the point to start at.

    `color` : the color and infill color of the shape, if applicable.

    `infill` : parameter that toggles infilling of shapes.

    `pensize` : The size of the pen to draw with.
    """
    # calculating angle
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
    # drawing shape
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



def write_to_screen(write_at:tuple, text:str, color:str, size:int):
    turt = Turtle()
    turt.hideturtle()
    turt.color(color)
    turt.speed(0)
    turt.penup()
    turt.goto(write_at)
    turt.write(text, font = ("arial", size, "normal"))