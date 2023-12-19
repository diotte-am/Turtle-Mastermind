This was the final project from my first semester of the 
<a href="https://www.khoury.northeastern.edu/programs/align-masters-of-science-in-computer-science">Align program at Northeastern</a>
 
Original Read Me (4/21):

I favored using classes for most Turtle parts of my program as I was having
 difficulty getting the Turtle and non-Turtle parts to talk to each other
 without using global variables. Each item that the user needs to click I
 initialized with it's own variable name so it would be easy to keep track
 of where it was and if it was being clicked. For the part of the game board
 that displays the guesses and bulls/cows, I set up for loops to iterate thru
 the # of columns and rows needed. I made fuctions where you can easily adjust
 the size of the marbles, distance between them, and even how many you want
 in a row and column. The boolean value in the parameters indicates whether
 you're drawing the "column" marbles in one line for the user guesses or
 you're drawing the bull+cows - where the number of columns is halved and
 two marbles print in each column. As the game board is set up, each new
 Marble object is saved to a list - 1 for the guess marbles and 1 for the
 bull and cow marbles. Each is a list of lists. Each inner list represents
 a round of the game, each marble within that list represents one guess or
 one bull/cow result. I created another Class of object Round to keep track
 of what round and guess the player is currently on. At any time the program
 is able to access those numbers so it know which marble to update the player
 interacts with the board. the turtle parts of my program are in the file
 game_board.py.

 Class BackgroundShapes are for objects in the turtle screen that are not
 interacted with. I used it for any of the pop ups that are triggered by
 events and the rounded rectangles in the background of my gameboard. Given
 more time, I'd ideally separate these into two different classes or make
 one a subclass of the other, but I didn't have enought time to really
 figure out how to do subclasses before deadline :(.

 Class Buttons are for any objects in the turtle screen that will be interacted
 with. This includes the 6 colored marble buttons and the gif images that are
 used as the quit/check/x button. Again, in a future interation, I'll probably
 separate the marble objects and the raster images buttons into different
 subclasses as their methods are a bit different.

 Extra credit - I allowed for duplicate colors in my count_bulls_and_cows.
 I created a copy of both the guess and secret code lists so I could
 delete each marble as I scored it, without messing up the index I was
 iterating over.
 
                                                    
