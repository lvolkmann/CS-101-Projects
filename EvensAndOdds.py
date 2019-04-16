##############################################################################################################
## CS 101
## EvensAndOdds(LV).py
## Program #3
## Landon Volkmann
## lsvr34@mail.umkc.edu
##
## PROBLEM   :
##  1. Simulate Game -- Evens & Odds -- based on user input, randomly generated numbers, and established rules
##  2. While playing, program asks user what type of game they would like to play (or quit)
##  3. Rounds/Matches won if user guess of even/odd matches sum of user and comp num
##  4. Run requested game simulation until victor declared
##  4. Repeat
##
## ALGORITHM :
##  While playing is True
##      Display menu and request input
##	    Validate with membership operator
##          if invalid
##	        warn user, display menu, and request input until valid
##
##	if user inputs option 1
##	    ask user how many rounds and request input (3-15 inclusive)
##	    validate with membership operator
##	    if invalid
##		warn user and request input until valid	
##          assign input to usr_rounds
##          assign the integer 0 to round_count
##	    assign the integer 0 to usr_score
##	    assign the integer 0 to comp_score
##	    assign ‘first’ to pick
##	    while round_count < usr_rounds
##	        prompt user for a number 1 to 5 inclusive
##		validate with membership operator
##		if invalid
##		    warn user and request input until valid
##		assign input to usr_num
##		if pick is equivalent to ‘first’
##		    randomly generate a number between 1 and 2 and assign to pick
##		if (pick % 2) is equivalent to 0
##		    prompt user to input even or odd
##		    validate with membership operator
##		    if invalid
##			warn user and request input until valid
##		    assign input to usr_even_odd
##		else
##	            assign ‘even’ or ‘odd’ at random to usr_even_odd
##		assign random integer from 1 to 5 to comp_num
##		assign (usr_num + comp num) % 2 to remainder
##		if remainder is equivalent to 0
##		    if usr_even_odd is equivalent to ‘even’
##		        add 1 to usr_score
##		    else
##			add 1 to comp_score
##		else
##			if usr_even_odd is equivalent to ‘odd’
##				add 1 to usr_score
##			else
##				add 1 to comp_score
##		add 1 to round_count
##		add 1 to pick
##
##	if user inputs option 2
##	    ask user how many rounds and request input (3-15 inclusive)
##	    validate with membership operator
##	    if invalid
##		warn user and request input until valid	
##          assign input to usr_rounds
##	    assign the integer 0 to round_count
##	    assign the integer 0 to usr_score
##	    assign the integer 0 to comp_score
##	    assign ‘first’ to pick
##	    while round_count < usr_rounds
##              assign integer 0 to usr_match
##		assign integer 0 to comp_match
##		while (usr_match is not equal to 2) AND (comp_match is not equal to 2)
##                  prompt user for a number 1 to 5 inclusive
##		    validate with membership operator
##		    if invalid
##		    	warn user and request input until valid
##		    assign input to usr_num
##		    if pick is equivalent to ‘first’
##		    	randomly generate number between 1 and 2 and assign to pick
##		    if (pick % 2) is equivalent to 0
##		    	prompt user to input even or odd
##		    	validate with membership operator
##		    	if invalid
##		    	    warn user and request input until valid
##			assign input to usr_even_odd
##		    else
##			assign ‘even’ or ‘odd’ at random to usr_even_odd
##		    assign random integer from 1 to 5 to comp_num
##		    assign (usr_num + comp num) % 2 to remainder
##		    if remainder is equivalent to 0
##			if usr_even_odd is equivalent to ‘even’
##		            add 1 to usr_match
##			else
##			    add 1 to comp_match
##		    else
##			if usr_even_odd is equivalent to ‘odd’
##		            add 1 to usr_match
##			else
##			    add 1 to comp_match
##		    add 1 to pick
##		if usr_match is equivalent to 2
##                  add 1 to usr_score
##		else
##                  add 1 to comp_score
##		add 1 to round_count
##
##	if user inputs ‘q’
##		assign False to playing
##
## ERROR HANDLING:
##  Program handles invalid input for:
##      User number choice (given input is an integer)
##      User number of rounds (given input is an integer)
##      User even or odd guess
##      
##############################################################################################################

#Modules:
import random
import time

#Functions:
def choose_number():
    """
This function returns an integer from 1 to 5 inclusive (1, 5). It will
continually ask the user for a number if they do not enter valid input until
they do.
"""
    valid = range(1,6)
    
    while True:
        usr_num = int(input("Enter an integer from 1 to 5 (inclusive): "))
        if usr_num in valid:
            return usr_num
        print("ERROR: INVALID INPUT")

def choose_number_of_rounds():
    """
This function takes no arguments and returns an integer. It will
continually ask the user for an integer input from 3 - 15, inclusive. ( 3, 15).
"""
    valid = range(3,16)
    
    while True:
        usr_num = int(input("Enter an integer from 3 to 15 (inclusive): "))
        if usr_num in valid:
            return usr_num
        print("ERROR: INVALID INPUT")

def gen_choose_num(lower_lim : int, upper_lim :int):
    """
This function takes two integer type arguments and returns an integer. The two arguments are the upper
and lower limit of valid number choices. This argument serves to consolidate the choose_number and choose_number_of_rounds functions.
The function will continually ask the user for a number if they do not enter valid input.
"""
    valid = range(lower_lim, (upper_lim + 1))
    
    while True:
        usr_num = int(input("\nEnter an integer from {} to {} (inclusive): ".format(lower_lim, upper_lim)))
        if usr_num in valid:
            return usr_num
        print("ERROR: INVALID INPUT")
        
def choose_even_or_odd():
    """
This function takes no arguments and returns a boolean ( True or
False). It returns True if the user choses even, and False if they do not.
"""
    while True:
        usr_even_odd = input("Even or Odd: ").upper()
        if usr_even_odd in ['E', 'EVEN']:
            return True
        if usr_even_odd in ['O', 'ODD']:
            return False
        print("ERROR: INVALID INPUT")
            
    
def is_match(even : bool, usr1_num : int, usr2_num : int):
    """
This function has 3 arguments and returns a boolean. Even indicates if the player choose the result to be
even or odd. It’s True if they choose even, False if they had chosen odd. The function returns
True if the result matches their prediction. If the numbers add up to an even number and the
even is True, then the function returns true.
"""
    remainder = (usr1_num + usr2_num) % 2
    time.sleep(2)
    if remainder == 0:
        if even == True:
            print("{} + {} = {} \nThat's an {} number! You {}".format(usr1_num, usr2_num, (usr1_num + usr2_num), 'even', 'win'))
            return True
        else:
            print("{} + {} = {} \nThat's an {} number! You {}".format(usr1_num, usr2_num, (usr1_num + usr2_num), 'even', 'lose'))
            return False
    else:
        if even == True:
            print("{} + {} = {} \nThat's an {} number! You {}".format(usr1_num, usr2_num, (usr1_num + usr2_num), 'odd', 'lose'))
            return False
        else:
            print("{} + {} = {} \nThat's an {} number! You {}".format(usr1_num, usr2_num, (usr1_num + usr2_num), 'odd', 'win'))
            return True
    
def print_menu():
    """
This funciton takes no arguments and returns a string.
It will print a menu and prompt for user input until
valid input is porvided.
"""
    valid = ['1', '2', 'Q']
    while True:
        usr_op = input("""
Welcome to Evens & Odds!

Please Enter One of the Following:
1 -> Play Singles
2 -> Play 2 Out of 3 Rounds
q -> Quit
""").upper()
        if usr_op in valid:
            return usr_op
        print("ERROR: INVALID INPUT")
        
def get_pick(pick_status):
    """
This function takes one argument of variable type and returns an intger.
It checks to see if it's the first round and randomly chooses a starting player
if it is the first round. Otherwise, it simply returns the argument passed (an integer determining
whose turn it is).
"""
    if pick_status == 'Start':
        pick_status = random.randint(1,2)
        if pick_status == 2:
            print("You were randomly chosen to pick first!\nYou lucky duck!")
            time.sleep(3)
        else:
            print("Your opponent was randomly chosen to pick first!\nSeriously, it was random. I promise...")
            time.sleep(3)
        return pick_status
    else:
        return pick_status
    
def do_pick(pick_status : int):
    """
This function takes one integer type argument and returns a boolean.
Pick Status = Even ==> return True (user's turn)
Pick Status = Odd ==> return False (comp's turn)
"""
    if (pick_status % 2) == 0:
        return True
    else:
        return False
    
#Main
#Loops until user prompts quit
playing = True
while playing == True:

    #print menu
    game_choice = print_menu()

    #reset counters each loop
    round_count = 0
    usr1_score = 0
    usr2_score = 0
    pick = 'Start'

    #Game option 1
    if game_choice == "1":

        #Get number of rounds
        print("How many rounds would you like to play?")
        total_rounds = gen_choose_num(3,15)

        #Loops until number of rounds requested are played
        while round_count < total_rounds:

            #Display standing at the beginning of each round
            time.sleep(2)
            print("\n- ROUND: {} of {} -  SCORE: {} to {} -".format(round_count, total_rounds, usr1_score, usr2_score))

            #Get user guess and comp guess
            usr1_num = gen_choose_num(1,5)
            usr2_num = random.randint(1,5)

            #If first round, randomly chooses starting player
            pick = get_pick(pick)

            #Get user even/odd guess or comp guess
            if do_pick(pick):
                e_bool = choose_even_or_odd()
            else:
                e_bool = random.choice([True, False])
                
                #The following printed results are inverted because e_bool represents the user's default choice
                if e_bool == True:
                    print("Your opponent chose odd.")
                else:
                    print("Your opponent chose even.")

            print("Your opponent chose {}".format(usr2_num))

            #Check if match and score accordingly
            result = is_match(e_bool, usr1_num, usr2_num)

            if result:
                usr1_score += 1
            else:
                usr2_score += 1

            #Log round number and alternate even/odd guess turn
            round_count += 1
            pick += 1

        #Display results
        print("Calculating results...")
        time.sleep(2.5)
        if usr1_score > usr2_score:
            print("\nYou won! You won {} of {} or {:.2f}% of the games\nThis is one for the fridge!".format(usr1_score, total_rounds, (100*(usr1_score / total_rounds))))
        elif usr1_score < usr2_score:
            print("\nYou lost! You only won {} of {} or {:.2f}% of the games\nReally... quite a poor job.".format(usr1_score, total_rounds, (100*(usr1_score / total_rounds))))
        else:
            print("\nYou tied! Winning {} of {} or {:.2f}% of the games\nWhat a splendidly neutral turn of events!".format(usr1_score, total_rounds, (100*(usr1_score / total_rounds))))

    #Game option 2
    if game_choice == '2':

        #Get number of rounds
        print("How many rounds would you like to play?")
        total_rounds = gen_choose_num(3,15)

        #Loops until number of rounds requested are played
        while round_count < total_rounds:

            #Display standing at the beginning of each round
            time.sleep(2)
            print("\n- ROUND: {} of {} -  SCORE: {} to {} -".format(round_count, total_rounds, usr1_score, usr2_score))

            #Reset counters each loop
            usr1_match = 0
            usr2_match = 0

            #Loops until either user or comp reaches 2 wins for round
            while ((usr1_match != 2) and (usr2_match != 2)):

                #Get user guess and comp guess
                usr1_num = gen_choose_num(1,5)
                usr2_num = random.randint(1,5)

                #If first round, randomly chooses starting player
                pick = get_pick(pick)

                #Get user even/odd guess or comp guess
                if do_pick(pick):
                    e_bool = choose_even_or_odd()
                else:
                    e_bool = random.choice([True, False])
                    
                    #The following printed results are inverted because e_bool represents the user's default choice
                    if e_bool == True:
                        print("Your opponent chose odd.")
                    else:
                        print("Your opponent chose even.")

                print("Your opponent chose {}".format(usr2_num))

                #Check if match and score accordingly
                result = is_match(e_bool, usr1_num, usr2_num)

                if result:
                    usr1_match += 1
                else:
                    usr2_match += 1

                #Alternate even/odd guess turn
                pick += 1

            #Score round based on winner of most matches
            if usr1_match > usr2_match:
                usr1_score += 1
            else:
                usr2_score += 1

            #Display round results    
            print("You won {} to your opponent's {}".format(usr1_match, usr2_match))

            #Log round
            round_count += 1

        #Display results
        print("Calculating results...")
        time.sleep(2.5)
        if usr1_score > usr2_score:
            print("\nYou won! You won {} of {} or {:.2f}% of the games\nThis is one for the fridge!".format(usr1_score, total_rounds, (100*(usr1_score / total_rounds))))
        elif usr1_score < usr2_score:
            print("\nYou lost! You only won {} of {} or {:.2f}% of the games\nReally... quite a poor job.".format(usr1_score, total_rounds, (100*(usr1_score / total_rounds))))
        else:
            print("\nYou tied! Winning {} of {} or {:.2f}% of the games\nWhat a splendidly neutral turn of events!".format(usr1_score, total_rounds, (100*(usr1_score / total_rounds))))

    #Quit (Exits Loop)
    if game_choice == 'Q':
        playing = False
        print("Miss you already!")
        time.sleep(.5)
        print("Thanks for playing!")
        time.sleep(1)
        print("Come again soon!")
        time.sleep(2)
        print("...please...")
        
