'''
Amare Diotte
CS 5001
Spring 2021
Final Project
'''

import turtle
from Point import Point

MARBLE_RADIUS = 15

class Marble:
    '''
    Class of turtle drawings
    '''
    def __init__(self, position, color, size = MARBLE_RADIUS):
        '''
        Method - Initializes marble object
        Parameters:
        Self - Marble
        Position - Tuple with x, y values
        Color -- String, indicates color of marble
        Size -- Radius of Marble - default value is constant
        '''
        self.pen = self.new_pen()
        self.pen.pencolor = (97, 72, 239)
        self.pen.pensize(2)
        self.color = color
        self.position = position
        self.visible = False
        self.is_empty = True
        self.pen.hideturtle()
        self.size = size
        self.pen.speed(0)  # set to fastest drawing

    def __str__(self):
        return "The Marble at {} has a radius of {}. It is {}".\
               format(position, size, color)

    def __eq__(self, other):
        if self.color == other.color:
            if self.position == other.color:
                if self.size == other.size:
                    return True
        return False

    def new_pen(self):
        '''
        Method - creates new Turtle
        Parameters -
        Self -- Marble
        Output:
        New turtle
        '''
        return turtle.Turtle()

    def set_color(self, color):
        '''
        Method - Sets color of marble before drawing
        Parameters:
        Self -- Marble
        Color -- String, indicates color
        Output: None
        '''
        self.color = color
        self.is_empty = False

    def draw(self):
        '''
        Method - Draws a circle
        Parameters:
        Self -- Marble
        Output -- None
        '''
        # if self.visible and not self.is_empty:
            # return
        self.pen.up()
        self.pen.goto(self.position.x, self.position.y)
        self.visible = True
        self.is_empty = False
        self.pen.down()
        self.pen.fillcolor(self.color)
        self.pen.begin_fill()
        self.pen.circle(self.size)
        self.pen.end_fill()

    def draw_empty(self):
        '''
        Method - Draws circle with no fill
        Parameters -
        Self -- Marble
        Output: None
        '''
        self.erase()
        self.pen.up()
        self.pen.goto(self.position.x, self.position.y)
        self.visible = True
        self.is_empty = True
        self.pen.down()
        self.pen.circle(self.size)

    def clicked_in_region(self, x, y):
        '''
        Method - indicates if marble has been clicked
        Parameters:
        Self - Marble
        x, y - number values from click action
        '''
        if abs(x - self.position.x) <= self.size * 2 and \
           abs(y - self.position.y) <= self.size * 2:
            return True
        return False

