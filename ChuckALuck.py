########################################################################
## CS 101
## ChuckALuck(LV).py
## Program #2
## Landon Volkmann
## lsvr34@mail.umkc.edu
##
## PROBLEM   :
##  1. Simulate a carnival game that relies on user inputs and randomly generated die.
##  2. User will be prompted for starting amount, wager, and die guess.
##  3. Guess will be compared to three randomly generated die rolls.
##  4. Starting amount will increase/decrease based on number of correct guesses.
##  5. Game ends when starting amount is less than or equal to zero.
##  6. Program will ask user if they would like to play again.
##
## ALGORITHM : 
##  Set playing to True
##  While playing is equivalent to true
##  Prompt user for starting amount input
##  Set pot_proposal equal to user input
##  While pot_proposal is less than 0
##      Give warning that input is invalid
##      Prompt user for starting amount input
##      Set pot_proposal equal to input
##  Set user_pot equal to pot_proposal
##  While user_pot is greater than zero
##      Display value of user_pot to user
##      Prompt user for wager input
##      Set wager_proposal to user input
##      While wager_proposal is less than or equal to 0 OR wager_proposal is greater than user_pot
##          Give warning that input is invalid
##          Prompt user for wager
##          Set wager_proposal equal to input
##      Set user_wager equal to wager_proposal
##      Prompt user to guess integer between 1 and 6 inclusive
##      Set guess_proposal equal to user input
##      While guess_proposal is not in the range of 1 to 7 exclusive
##          Give warning that input is invalid
##          Prompt user for guess input
##          Set guess_proposal equal to input
##      Set user_guess equal to guess_proposal
##      Set die1 equal to random integer between 1 and 6 inclusive
##      Set die2 equal to random integer between 1 and 6 inclusive
##      Set die3 equal to random integer between 1 and 6 inclusive
##      Create set dice to contain die1, die2, and die3
##      Set match_count equal to zero
##      For each variable in container dice
##          If the variable is equivalent to user_guess
##              Add 1 to match_count
##          If match_count is greater than zero
##              Add match_count times user_wager to user_pot
##          Else
##              Subtract user_wager from user_pot
##  Create cont_responses to contain “NO”, “N”, “YES”, and “Y”
##  Ask user if they would like to play again
##  Set cont_proposal equal to user input
##  While cont_proposal is not in cont_responses
##      Give warning that input is invalid
##      Prompt user for input
##      Set cont_proposal equal to user input
##  Set user_cont equal to cont_proposal
##  If user_cont is equivalent to either “NO” or “N”
##      Set playing to False    
## 
## ERROR HANDLING:
##  Program handles invalid user input for:
##      Starting amount (provided input is some type of integer)
##      Wager (provided input is some type of integer)
##      Dice Guess
##      Continue Game Input
##      
########################################################################

#Module imported for die rolls
import random

playing = True

#The Game
while playing:

    round_count = 0
    
    #Prompt user for starting amount
    pot_proposal = int(input("How much money do ya got?:\n"))
    while pot_proposal < 0:
        print("ERROR! Invalid Input!")
        pot_proposal = int(input("I said, 'How much MONEY do ya got'. I prefer positive integers. So?:\n"))
    user_pot = pot_proposal

    #Loops until user runs out of money
    while user_pot > 0:

        round_count += 1
        print("\nYou have,", user_pot, "dollar(s) left.")

        #Prompt user for wager
        wager_proposal = int(input("How much would you like to wager?:\n"))
        while (wager_proposal <= 0) or (wager_proposal > user_pot):
            print("ERROR! Invalid Input!")
            wager_proposal = int(input("No seriously. What's your wager? Like a real wager?:\n"))
        user_wager = wager_proposal

        #Promt user for guess
        guess_proposal = int(input("Alright! Guess a number between one and six (including six):\n"))
        while guess_proposal not in range(1,7,1):
            print("ERROR! Invalid Input!")
            guess_proposal = int(input("Okay... That was a dumb guess... Please... Try again. What's your guess?:\n"))
        user_guess = guess_proposal

        #Three simulated die rolls
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        die3 = random.randint(1,6)

        dice = [die1, die2, die3]

        #Calculates number of die guessed correctly
        match_count = 0
        for roll in dice:
            print('You rolled a', roll)
            if roll == user_guess:
                match_count += 1
                
        #Returns number of die guessed correctly and corresponding winnings
        #0 Correct: Lose wager
        #1 Correct: Keep wager and win wager amount
        #2 Correct: Keep wager and win 2 times wager amount
        #3 Correct: Keep wager and win 3 times wager amount
        print("You got,", match_count, "right!")
        if match_count > 0:
            print('Congratulations! You get %d dollar(s) back!' % (user_wager * match_count))
            user_pot += (user_wager * match_count)
        else:
            print('Bad luck! You lost your wager of %d dollar(s)' % (user_wager))
            user_pot -= user_wager
            
    #Ask user if they would like to keep playing       
    cont_responses = ['NO','N','YES','Y', 'YEAH', 'YEP']
    print("\nYou're all out of money after just %d round(s)!" % (round_count))
    cont_proposal = input("Would you like to play again?:\n").upper()
    while cont_proposal not in cont_responses:
        print("ERROR! Invalid Input!")
        cont_proposal = input("Would you like to play again?:\n").upper()
    user_cont = cont_proposal

    #If user did not want to continue, ends game
    if (user_cont == 'NO') or (user_cont == 'N'):
        playing = False
