'''
Amare Diotte
CS 5001
Spring 2021
Final Project
'''

import turtle
from Point import Point

class BackgroundShapes:
    '''
    Class of turtle shapes. Rounded rectangles drawn in background for aesthetic
    reasons. User does not interact
    with them
    '''
    def __init__(self, position, color, length, height, radius):
        '''
        Method - initializes BackgroundShape, a rounded rectangle
        Parameters:
        self -- BackgroundShape object
        position -- Tuple that is x,y location
        color -- String, describes color of BackgroundShape
        length -- Int/Float -- length of shape
        height -- Int/Float -- height of shape
        radius -- Int/Float -- radius of corner
        '''
        self.pen = self.new_pen()
        self.color = color
        self.position = position
        self.pen.hideturtle()
        self.length = length
        self.height = height
        self.radius = radius
        self.pen.speed(0)

    def new_pen(self):
        '''
        Method - creates a new turtle object
        Parameters:
        Self -- BackgroundShape object
        Output -- Turtle object
        '''
        return turtle.Turtle()

    def rounded_rectangle(self):
        '''
        Method - draws a rounded rectangle at self.position
        Parameters:
        Self -- a BackgroundShape
        Output:
        None
        '''
        self.pen.up()
        self.pen.goto(self.position.x, self.position.y)
        self.pen.down()
        self.pen.pencolor(153, 246, 208)
        self.pen.pensize(5)
        self.pen.fillcolor(self.color)
        self.pen.begin_fill()
        for i in range(2):
            self.pen.forward(self.length)
            self.pen.circle(self.radius, 90)
            self.pen.forward(self.height)
            self.pen.circle(self.radius, 90)
        self.pen.end_fill()

    def draw_text(self, text):
        '''
        Method - draws text within the BackgroundShape
        Parameters:
        Self -- a BackgroundShape
        Text -- string
        Output:
        None
        '''
        number = text[:1]
        name = text[2:]
        self.pen.up()
        self.pen.goto(self.position.x, self.position.y)
        self.pen.write(number, font=("Helvetica", 16, "bold"))
        self.pen.goto(self.position.x + 15, self.position.y - 11)
        self.pen.write(name, font=("Helvetica", 12))

    def line_skip(self, y):
        '''
        Method - when writing to screen, adds extra space between lines of text
        Parameters:
        Self -- BackgroundShape
        y -- int or float, indicates size of added space between lines
        Output:
        None
        '''
        self.position.y -= y
        

