########################################################################
## CS 101
## PySnake(LV).py
## Program #5
## Landon Volkmann
## lsvr34@mail.umkc.edu
##
## PROBLEM   :
##  1. Show beginning screen with instructions
##  2. Play snake game
##      2a. If snake hits wall or body => Lose
##      2b. If snake eats food => score and snake length increment by 1
##  3. After loss, display score and ask to play again
##
## ALGORITHM :
##
##  FUNCTIONS
##  Def get_last_key()
##      Returns last key entered
##  Def display_menu()
##      Draw text on screen (350,350, “Directions”)
##      Draw Screen
##  Def display_game_over()
##      Draw text on screen (350,350, “Game Over; Directions”)
##      Draw Screen
##  Def random_coordinate()
##      Cord is assigned an empty list
##      X = random integer in range 0 to 700 step 20
##      Y = random integer in range 0 to 681 step 20
##      Append x to cord
##      Append y to cord
##      Return cord
##  Def check_valid_key(key, new_key)
##      If new_key not in valid_keys
##          Return false
##      Pair is assigned key, new_key
##      If pair in opposites
##          Return false
##      Else
##          Return True
##  Def get_food_cord(snake_cord)
##      Snake_instance is assigned an empty list
##      For x in snake_cord
##          Append tuple form of x to snak_instance
##      While True
##          Cord is assigned the result of random_coordinate()
##          If cord not in snake_instance
##              Return cord
##  Def play_again()
##      Valid is assigned list [“Up”, “Down”]
##      Answ is assigned an empty string
##      While answ not in valid
##          Display_game_over()
##          Answ is assigned get_last_key()
##      If answ is equal to “Up”
##          Return true
##      If answ is equal to “Down”
##          Return False
##  
##  MAIN
##  Valid_keys is assigned list ["Up", "Down", "Right", "Left"]
##  Opposites is assigned list [("Up", "Down"), ("Down", "Up"), ("Left", "Right"), ("Right", "Left")]
##  Win is assigned a window (700 by 700)
##  Window is assigned True
##  While window is equal to True:
##      Playing is assigned True:
##      Snake_cord is assigned an empty list
##      New_cord is assigned result of random_coordinate
##      Append new_cord to snake_cord
##      Key is set equal to an empty string
##      While key is not in valid_keys:
##          Display_menu()
##          Key is assigned result of get_last_key
##      Food_cord is assigned the result of get_food_cord(snake_cord)
##      Score is set equal to 1
##      While playing is equal to true
##          New_key is assigned the result of get_last_key()
##          If check_valid_key(key,new_key) is true
##              Key = new_key
##          If key is equal to “Up”
##              Insert [snake_cord[0][0], snake_cord[0][1] - 20] into snake_cord at 0
##          Elif key is equal to “Down”
##              Insert [snake_cord[0][0], snake_cord[0][1] + 20] into snake_cord at 0
##          Elif key is equal to “Right”
##              Insert [snake_cord[0][0] + 20, snake_cord[0][1]] into snake_cord at 0
##          Elif key is equal to “Left”
##              Insert [snake_cord[0][0] - 20, snake_cord[0][1]] into snake_cord at 0
##          Head_cord is assigned snake_cord[0]
##          Body_cord is assigned an empty list
##          If food_cord is equal to head_cord
##              Append head_cord to snake_cord
##              Food_cord is assigned the result of get_food_cord(snake_cord)
##              Score is incremented by 1
##          Elif head_cord[0] is less than 0 or head_cord[0] is greater than 680
##              Playing is set equal to False
##          Elif head_cord[1] is less than 0 or head_cord[1] is greater than 680
##              Playing is set equal to False
##          Pop last item in snake_cord out of list
##          For cord in snake_cord
##              Append cord to body_cord
##          Remove head_cord from body_cord
##          If head_cord is in body_cord
##              Playing is set equal to False
##          For cord in snake_cord
##              Draw a rectangle -> (cord[0],cord[1], cord[0] + 20, cord[1] + 20, "Blue")
##          Draw a rectangle -> (food_cord[0], food_cord[1], food_cord[0] + 20, food_cord[1] + 20, "Red")
##          Wait for 1/10 of a second
##          Draw screen
##      Window is assigned the result of play_again()
##  
## ERROR HANDLING:
##  1. Key validation for snake direction input
##      1a. Key is up, down, left, or right
##      1b. Key is not directly opposite of current direction
##  2. Validates input for play_again prompt
##  3. Program does not crash upon closing window
##
########################################################################

#Modules
import python_graphics as gfx
import time
import random

#Screens
menu = """
Welcome to PySnake!
Use the Arrow Keys to control the direction of the snake
Gobble up the food to gain points and snake length
Be careful not to run into the walls or yourself

Press an arrow key to begin!
"""

game_over = """
Score: {}

Game Over...
You killed your snake...
I hope you're happy...

Press up to play again!
Press down to quit running the program
"""

#Validation Lists
valid_keys = ["Up", "Down", "Right", "Left"]
opposites = [("Up", "Down"), ("Down", "Up"), ("Left", "Right"), ("Right", "Left")]

#Functions
def display_menu():
    """Displays Menu Screen"""
    win.draw_text(350, 350, menu, "Red")
    win.draw_screen()

def display_game_over():
    """Displays Game Over Screen"""
    
    win.draw_text(350, 350, game_over.format(score), "Red")
    win.draw_screen()

def rand_cord(width : int, height : int):
    """Pass width and heeight of the window
    Returns one random coordinate within given window space
    Steps by 20s
    """
    cord = []
    x = random.randrange(0,width - 19,20)
    y = random.randrange(0,height - 19,20)
    cord.append(x)
    cord.append(y)
    return cord

def check_valid_key(key : str, new_key : str, valid_keys : list):
    """Pass last key used and new key in question
    Returns bool
    If valid => True
    If invalid => False
    """
    if new_key not in valid_keys:
       return False 
    pair = key, new_key
    if pair in opposites:
        return False
    else:
        return True
    
def get_food_cord(width : int, height : int, snake_cord : list):
    """Pass width and height of the window AND list of coordinates describing snake location
    will not generate coordinates that snake currently occupies
    returns coordinates in form of tuple
    """
    snake_instance = []
    for x in snake_cord:
        snake_instance.append(tuple(x))
    while True:
        cord = tuple(rand_cord(width, height))
        if cord not in snake_instance:
            return cord
        
def play_again():
    """Requests input from user
    if answer UP = True
    if answer DOWN = False
    returns bool
    """
    valid = ["Up", "Down"]
    answ = ''
    while answ not in valid:
        display_game_over()
        answ = win.get_last_key()
    if answ == "Up":
        return True
    if answ == "Down":
        return False



#Main Code
    
#Ensures progrma doesn't crash upon closing
try:

    #window parameters
    win = gfx.Window(700,700, "PySnake")
    #window running status
    window = True

    #Window stops refreshing when false
    while window:

        #Game status
        playing = True

        #Reset starting position
        snake_cord = []
        new_cord = rand_cord(700,700)
        snake_cord.append(new_cord)

        #Reset key
        key = ''

        #Displays menu until valid key entered
        while key not in valid_keys:
            display_menu()
            key = win.get_last_key()

        #Reset food starting position
        food_cord = get_food_cord(700,700, snake_cord)

        #Score
        score = 1

        #Game ends when snake dies
        while playing:

            #Get direction
            new_key = win.get_last_key()
                    
            if check_valid_key(key,new_key, valid_keys):
                key = new_key

            #Apply direction
            if key == "Up":
                snake_cord.insert(0,[snake_cord[0][0], snake_cord[0][1] - 20])
            elif key == "Down":
                snake_cord.insert(0,[snake_cord[0][0], snake_cord[0][1] + 20])
            elif key == "Right":
                snake_cord.insert(0,[snake_cord[0][0] + 20, snake_cord[0][1]])
            elif key == "Left":
                snake_cord.insert(0,[snake_cord[0][0] - 20, snake_cord[0][1]])

            #Distinguish b/w head and body    
            head_cord = tuple(snake_cord[0])
            body_cord = []

            #Win/Lose conditions
            #Get food, increment score, and increase snake length
            if food_cord == head_cord:
                snake_cord.append(list(head_cord)) 
                food_cord = get_food_cord(700,700, snake_cord)
                score += 1
            #Head off the screen vertically or horizontally => LOSE
            elif head_cord[0] < 0 or head_cord[0] > 680:
                playing = False
            elif head_cord[1] < 0 or head_cord[1] > 680:
                playing = False

            #Snake stretches forward and tail piece disappears
            snake_cord.pop()

            #populate body coordinates
            for cord in snake_cord:
                body_cord.append(tuple(cord))
                
            body_cord.remove(head_cord)

            #Head runs into body => LOSE
            if head_cord in body_cord:
                playing = False

            #Draw Snake               
            for cord in snake_cord:
                win.draw_rect(cord[0],cord[1], cord[0] + 20, cord[1] + 20, "Blue")

            #Draw food                      
            win.draw_rect(food_cord[0], food_cord[1], food_cord[0] + 20, food_cord[1] + 20, "Red")

            #Speed
            time.sleep(.1)

            #Output Screen
            win.draw_screen()

        #Ask uses to play again
        window = play_again()

    #Program no longer running and screen no longer refreshing    
    win.draw_text(350, 350, "Program no longer running. \nSee ya later!", "Red") 
    win.draw_screen()

#Close window without program crash    
except:
    print("Goodbye")




