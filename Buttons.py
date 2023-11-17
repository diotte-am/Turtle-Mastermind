'''
Amare Diotte
CS 5001
Spring 2021
Final Project
'''

import turtle
from Point import Point

class Button:
    '''
    A class of objects able to be clicked and also display a gif image
    '''
    def __init__(self, position, size_x, size_y):
        '''
        Method - initializes a Button
        Parameters:
        Self - Button object
        Position - tuple with number values for x, y
        size_x - width of Button
        size_y -- height of Button
        '''
        self.pen = self.new_pen()
        self.position = position
        self.visible = False
        self.is_empty = True
        self.pen.hideturtle()
        self.size_x = size_x
        self.size_y = size_y
        self.pen.speed(0)  # set to fastest drawing

    def __eq__(self, other):
        '''
        Method - compares two Button objects
        Parameters:
        Self -- Button
        Other -- different Button
        Output -- Boolean - True if equal, False if not
        '''
        if self.position == other.position:
            if self.visible == other.visible:
                if self.is_empty == other.is_empty:
                    if self.size_x == other.size_x:
                        if self.size_y == other.size_y:
                            return True
        return False

    def __str__(self):
        '''
        Method - returns a string describing the size and location of button
        Parameters:
        Self -- Button
        Output -- A string
        '''
        return "Button is {} wide by {} tall and is located at x:{}, y:{}"\
               .format(self.size_x, self.size_y, self.position.x, self.position.y)

    def new_pen(self):
        '''
        Method - create new turtle object
        Parameters: None
        Self -- Button object
        Output -- Turtle object
        '''
        return turtle.Turtle()

    def set_image(self, file):
        '''
        Method - Displays gif image at position
        Input:
        Self -- Button object
        String -- name of gif file
        Output -- none
        '''
        self.button = turtle.Turtle()
        self.button.up()
        self.button.goto(self.position.x, self.position.y)
        self.button.shape(file)

    def clicked_in_region(self, x, y):
        '''
        Method - compares clicked coordinates vs. coordinates of given shape,
        returns True if clicked in area of object, returns False if not
        Parameters:
        Self -- Button object
        2 Ints -- x and y position of most recent click
        Output -- Boolean, True if the click is near object, false if not
        '''
        if abs(x - self.position.x) <= self.size_x and \
           abs(y - self.position.y) <= self.size_y:
            return True
        return False

    def delete_shape(self):
        '''
        Method - deletes gif image displayed in Turtle screen
        Parameters:
        Self -- Button object
        Output -- None
        '''
        self.button.hideturtle()
