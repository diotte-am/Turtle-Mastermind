'''
Amare Diotte
CS 5001
Spring 2021
Final Project
'''


import turtle
from Marble import *
from Point import Point
from Buttons import Button
from Round import Round
from BackgroundShapes import BackgroundShapes

def draw_gameboard(start_x, start_y, row_range, column_range, half_column, \
                   delta_x, delta_y, radius):
    '''Draw gameboard - draws grids of Marble objects and returns a list of
       lists containing those objects. Marble obects draw w/white fill.
       Parameters:
       start_x, start_y: int or float. Indicates where the top left corner of
       the grid will start
       row_range, column_range: positive int. Indicates how many horizontal
       "rows" and vertical "columns" of Marble objects will be drawn.
       half_column: boolean True = instead of n columns with 1 Marble in each,
       draws n/2 colums with 2 in each (used for bull and cow board)
       delta_x, delta_y: int of float. Indicates the amount of space in between
       the start point of each Marble object.
       radius: int or float Indicates radius of Marble object
       Output: A list of lists - Each inner list represents 1 row on the game
       board or 1 game "round." 
    '''
    game_board = {}
    y = start_y
    for row in range(row_range):
        round_list = []
        round_number = row
        x = start_x
        for column in range(column_range):
            marble = Marble(Point(x, y), 'white', size = radius)
            marble.draw()
            round_list.append(marble)
            x += delta_x
        if not half_column:
            game_board[round_number] = round_list
        elif half_column:
            y += delta_y
            x = start_x
            for column in range(column_range):
                marble = Marble(Point(x, y), 'white', size = radius)
                marble.draw()
                round_list.append(marble)
                x += delta_x
            y += delta_y / 2
            game_board[round_number] = round_list
        y += delta_y
    return game_board

def display_leaderboard(sorted_scores):
    '''
    Draws leaderboard in turtle screen and displays winners as text inside it
    Parameters: sorted lists
    Output: none
    '''
    leader_board = BackgroundShapes(Point(-65, 245), (228, 255, 238), 0, 0, 0)
    for each in sorted_scores: 
        leader_board.draw_text(each)
        leader_board.line_skip(40) 
  
def bye():
    '''
    Quits turtle screen
    Parameters: None
    Output: none
    '''
    turtle.bye()

def get_name():
    '''
    Opens input box in turtle screen. Input is stored as players name. If no
    name provided, defaults to "Anonymous Turtle"
    Parameters: None
    Output: String
    '''
    name = turtle.textinput("Welcome to Mastermind!", "Please enter your name:")
    if name == "" or name == None:
        name = "Anonymous Turtle"
    return name

def update_gameboard_color(color, guess, game_board, game_round, guess_counter):
    '''
    Updates the color of the corresponding marble on the game_board when players
    clicks one of the color marbles in user input
    Inputs:
    color - string: the color of the marble clicked
    guess - list: list of colors guessed so far
    game_board - list: list of Marble objects making up the game_board
    Output: none
    '''
    if len(guess) <= 3:
        guess.append(color)
        game_board[game_round.current][guess_counter.current].set_color(color)
        game_board[game_round.current][guess_counter.current].draw()
        guess_counter.add()    



