'''
Amare Diotte
CS 5001
Spring 2021
Final Project
'''


class Round:
    '''
    Class - counter that keeps track of what round the game is in
    '''
    def __init__(self, start, end):
        '''
        Method - Initializes a Round 
        Parameters:
        Self -- a Round
        Start -- int: indicates what round to start on
        End -- int: indicates what round to end on
        Output:
        None
        '''
        if not isinstance(start, int):
            raise ValueError
        else:
            self.start = start
            self.current = start
        if not isinstance(end, int):
            raise ValueError
        else:
            self.end = end
        
    def __eq__(self, other):
        '''
        Method - Compares two rounds to see if current value is equal
        Parameters:
        Self -- a Round
        Other -- a Round
        Output -- a boolean: True if current round of two Rounds equal
        '''
        if self.current == other.current:
            return True
        else:
            return False

    def __str__(self):
        '''
        Method - returns a string indicating the current round
        Self -- A round
        Output -- a string
        '''
        return "The current round is {}".format(self.current)

    def add(self):
        '''
        Method - advances current round by 1
        Parameters:
        Self -- a Round
        Output -- none
        '''
        self.current += 1

    def subtract(self):
        '''
        Method - subtracts 1 from current round
        Parameters:
        Self -- a Round
        Output -- none
        '''
        self.current -= 1

    def set_to_zero(self):
        '''
        Method - sets current round to 0
        Parameters:
        Self -- a Round
        Output -- none
        '''
        self.current = 0
