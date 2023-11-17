'''
Amare Diotte
CS 5001
Spring 2021
Final Project
'''


from random import randint
import turtle
from Marble import *
from Point import Point
from Buttons import Button
from game_board import draw_gameboard, display_leaderboard, bye, get_name, update_gameboard_color
from Round import Round
from BackgroundShapes import BackgroundShapes

MARBLE_COLORS = ["blue", "red", "yellow", "green", "purple", "black"]

def generate_code():
    '''
    Generates random 4 color code at the start of each game. Duplicate colors
    allowed
    Input: None
    Output: list with 4 color names
    '''
    secret_code = []
    for i in range(4):
        marble = randint(0, 5)
        secret_code.append(MARBLE_COLORS[marble])
    return secret_code


def count_bulls_and_cows(secret_code, guess):
    '''
    Checks user guess against the secret code, returns the number of
    "bulls" and "cows"
    Input - 2 lists with 4 items each. One list is the solution, one is
    the user's guess.
    Output - 1 tuple of 2 integers
    '''
    # copy of each list will keep track of which marbles counted
    copy_secret = secret_code.copy()
    copy_guess = guess.copy()
    bull, cow = 0, 0
    for i in range(len(guess)):
        # if marble is in correct position & color
        if guess[i] == secret_code[i]:
            bull += 1
            # get rid of marble from lists so it's not counted twice
            copy_secret.remove(guess[i])
            copy_guess.remove(guess[i])
    # gets number of remaining marbles to check
    cow_range = len(copy_guess)
    for i in range(cow_range):
        # if marble correct color, wrong position
        if copy_guess[i] in copy_secret:
            cow += 1
            # get rid of marble from the list so it's not counted twice
            copy_secret.remove(copy_guess[i])
    return bull, cow

def load_winners(file_name):
    '''
    Opens file containing a list of past winners. Saves the names and scores
    to a list and then sorts them by score in ascending order.
    Parameters: string - Name of file to be opened.
    Output: sorted list of int(score) & string(name)
    '''
    stored_scores = []
    with open(file_name, "r") as infile:
        for each in infile:
            stored_scores.append(each)
            stored_scores.sort()
            # limits list to top 10 scores
            if len(stored_scores) > 10:
                stored_scores = stored_scores[:10]

    return stored_scores

def game_driver():
    '''
    Runs functions to set up game board, load leaderboard, get user name
    Contains nested function for onclick
    Parameters: None
    Output: None
    '''
    window = turtle.Screen()
    window.title("~*~*~*~*~ MASTERMIND ~*~*~*~*~")
    window.colormode(255)
    window.bgcolor(184, 178, 207)
    window.setup(900, 800)
    window.addshape("checkbutton.gif")
    window.addshape("xbutton.gif")
    window.addshape("quit.gif")
    window.addshape("quitmsg.gif")
    window.addshape("Lose.gif")
    window.addshape("winner.gif")
    window.addshape("leaderboard_error.gif")
    window.addshape("leaderboard.gif")
    window.addshape("mastermindtitle.gif")
    
    game_round = Round(0, 9)
    guess_counter = Round(0, 4)

    background = BackgroundShapes(Point(-375, -234), (228, 255, 238), 550, 40, 10)
    background.rounded_rectangle()

    background = BackgroundShapes(Point(-375, -140), (228, 255, 238), 265, 450, 10)
    background.rounded_rectangle()

    background = BackgroundShapes(Point(-70, -140), (228, 255, 238), 240, 450, 10)
    background.rounded_rectangle()

    red = Marble(Point(-350, -220), "red")
    red.draw()

    blue = Marble(Point(-300, -220), "blue")
    blue.draw()

    green = Marble(Point(-250, -220), "green")
    green.draw()

    yellow = Marble(Point(-200, -220), "yellow")
    yellow.draw()

    purple = Marble(Point(-150, -220), "purple")
    purple.draw()

    black = Marble(Point(-100, -220), "black")
    black.draw()

    quit_button = Button(Point(135, -205), 30, 15)
    quit_button.set_image("quit.gif")

    x_button = Button(Point(5, -205), 15, 15)
    x_button.set_image("xbutton.gif")

    check_button = Button(Point(-30, -205), 15, 15)
    check_button.set_image("checkbutton.gif")

    leaderboard_error = Button(Point(0, 0), 15, 15)

    quit_message = Button(Point(0, 0), 15, 15)

    lose_message = Button(Point(0, 0), 15, 15)

    leaderboard = Button(Point(50, 300), 150, 29)
    leaderboard.set_image("leaderboard.gif")

    mastermind = Button(Point(225, 90), 50, 350)
    mastermind.set_image("mastermindtitle.gif")

    # input from Turtle screen
    name = get_name()
    guess = []
    secret_code = generate_code()
    # grid of Marbles showing guesses
    game_board = draw_gameboard(-350, 280, 10, 4, False, 45, -45, MARBLE_RADIUS)
    # grid of Marbles showing bulls & cows
    bull_cow = draw_gameboard(-150, 299, 10, 2, True, 18, -18, 6)
    try:
        sorted_scores = load_winners("high_scores.txt")
        display_leaderboard(sorted_scores)
    except:
        leaderboard_error.set_image('leaderboard_error.gif')
        #shows error window but game continues..
        window.ontimer(leaderboard_error.delete_shape, 1000)
    def get_click(x, y):
        '''
        Links actions to mouseclick event.
        Parameters: x, y location of mouseclick
        Output: None
        '''
        location = Point(x,y)

        if quit_button.clicked_in_region(x, y):
            quit_message.set_image('quitmsg.gif')
            print("See you soon, {}!".format(name))
            window.ontimer(bye, 1000)
            
        if x_button.clicked_in_region(x, y):
            # removes last guess from list and gameboard
            if guess != []:
                guess.pop()
                guess_counter.subtract()
                game_board[game_round.current][guess_counter.current].set_color("white")
                game_board[game_round.current][guess_counter.current].draw()
                
        if check_button.clicked_in_region(x, y):
            # processes results after guess is submitted
            if len(guess) == 4:
                results = count_bulls_and_cows(secret_code, guess)
                bull, cow = results
                # color bull marbles to black
                for i in range(int(bull)):
                    bull_cow[game_round.current][i].set_color("black")
                    bull_cow[game_round.current][i].draw()
                # color cow marbles to red
                for j in range(int(cow)):
                    bull_cow[game_round.current][int(bull) + j].set_color("red")
                    bull_cow[game_round.current][int(bull) + j].draw()
                # lose message after 10 rounds
                if game_round.current == 9 and bull != 4:
                    quit_message.set_color('Lose.gif')
                    window.ontimer(bye, 1000)
                # victory message
                if bull == 4:
                    with open('high_scores.txt', mode='a') as high_scores:
                        high_scores.write(str(game_round.current + 1) + " " +\
                                          name[:33] + "\n")
                    quit_message.set_image('winner.gif')
                    print("Congrats! Thanks for playing, {}!".format(name))
                    window.ontimer(bye, 1000) 
                # round ends here
                # round + 1, guess count and guess list are cleared
                game_round.add()
                guess_counter.set_to_zero()
                guess.clear()
        if len(guess) <= 4:
            # marbles in game board changed to color of the marble object
            # user has clicked
            if red.clicked_in_region(x, y):
                update_gameboard_color("red", guess, game_board, game_round, guess_counter)
                
            elif blue.clicked_in_region(x, y):
                update_gameboard_color("blue", guess, game_board, game_round, guess_counter)

            elif green.clicked_in_region(x, y):
                update_gameboard_color("green", guess, game_board, game_round, guess_counter)

            elif yellow.clicked_in_region(x, y):
                update_gameboard_color("yellow", guess, game_board, game_round, guess_counter)
                
            elif purple.clicked_in_region(x, y):
                update_gameboard_color("purple", guess, game_board, game_round, guess_counter)
                
            elif black.clicked_in_region(x, y):
                update_gameboard_color("black", guess, game_board, game_round, guess_counter)
          
    window.onclick(get_click)
    window.mainloop()
def main():
    game_driver()

    


if __name__ == "__main__":
    main()

