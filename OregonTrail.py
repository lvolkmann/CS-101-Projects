########################################################################
##
## CS 101
## Program #7
## Landon Volkmann
## lsvr34@mail.umkc.edu
##
## PROBLEM :
##
##  1. Simulate Orgeon Trail
##  2. Game ends when one of exit conditions met:
##      a. All settlers dead
##      b. Destination reached
##      c. Run out of food
##
## ALGORITHM :
##
##  //Initialize Wagon & Settlers
##  wagon = Wagon(2000)
##  wagon.settlers.append( Person("Player1"))
##  wagon.settlers.append( Person("Player2"))
##  wagon.settlers.append( Person("Player3"))
##  wagon.settlers.append( Person("Player4"))
##  wagon.settlers.append( Person("Player5"))
##  
##  //Iterates over trail until they get to the destination or lose
##  While not wagon.game_over():
##  	Print(wagon)
##  	choice = input()
##  	if choice == “1”: //Move wagon
##  		wagon.move()
##  	elif choice == “2”: //Change pace
##  		pace_choice = input()
##  		wagon.pace = int(pace_choice)
##  	elif choice == “3”: // Change ration
##  		ration_choice = input()
##  		wagon.ration = int(ration_choice)
##  	elif choice == “4”: //Rest
##  		rest_days = input()
##  		wagon.rest(rest_days)
##  	elif choice == “5”: //Output Settlers
##  		print(“Settlers “)
##  		for settler in wagon.settlers:
##  			print(settler)
## 
## ERROR HANDLING:
##
##  1. Validate input from user
##  2. Health may not exceed 100
##
########################################################################

import random


class Person(object):

    def __init__(self, name : str):
        """ Initializes a Person with their name, and sets their health to 100
        :param name: str - The name of the settler
        :return:
        """
        self.name = name
        self.health = 100
        if name == "Kristopher":
            self.modes_of_death = ['a broken heart']
        else:
            self.modes_of_death = ['drowning', 'dysentery', 'suffocation in a freak fire', 'a mule kick', 'starvation', 'a broken heart', 'dehydration', 'sun poisoning', 'tetnus', 'botched amputation', 'an asthma attack', 'cannibalism', 'the proletariat uprising']
        

    def __str__(self):
        """
        :return: str  Format with the name_-_health of the person
        """
        return "{} - {}".format(self.name, self.health)

class Wagon(object):

    
    def __init__(self, food : int):
        """ Sets up an instance of the wagon.
        :param food: The amount of food in pounds on the wagon.
        :return:
        :attributes to set
            food : int - Food passed in as paramter
            mile : int - How many miles the wagon has travelled   Initialize to 0.
            settlers : list - Create an empty list of the settlers ( instances of Person )
            pace : int - How fast the settlers will be moving.
                1 - slow, 2 - moderate, 3 - fast
            rations : int - Rationing setting for the setllers
                1 - normal ration, 2 - small ration, 3 - limited rations
            day : int - The day of the adventure.  Starts at 1.
        """
        self.settlers = []
        self.food = food
        self.mile = 0
        self.pace = 2
        self.rations = 1
        self.day = 1
        

    def pace_str(self):
        """ Returns a string representation of the pace
        :return: str -
                    If pace is 1, return 'slow'
                    If pace is 2, return 'moderate'
                    If pace is 3, return 'fast'
        """
        if self.pace == 1:
            return 'slow'
        if self.pace == 2:
            return 'moderate'
        if self.pace == 3:
            return 'fast'
        

    def ration_str(self):
        """ Return a string representation of the rations
        :return: str -
                    If ration is 1, return 'normal'
                    If ration is 2, return 'small'
                    If ration is 3, return 'starving'
        """
        if self.rations == 1:
            return 'normal'
        if self.rations == 2:
            return 'small'
        if self.rations == 3:
            return 'starving'

    def group_health(self):
        """ Returns back a string of how the settlers are doing.
        :return: str -
            If the average health of all the settlers alive is > 80, then return 'good'
            If the average is > 50 return 'fair'
            otherwise, return 'poor'
        """
        
        total_health = 0
        for settler in self.settlers:
            total_health += settler.health
        average = total_health/len(self.settlers)
        
        if average > 80:
            return 'good'
        elif average > 50:
            return 'fair'
        else:
            return 'poor'
                

    def __str__(self):
        """ Returns a String representation of the wagon  Shown below
        :return: - str

Wagon is at 0 mile on day 1
You have 2000 pounds of food left
You are moving at moderate pace with normal rations
Settlers are in good health

        """
        return """
Wagon is at {} mile on day {}
You have {} pounds of food left
You are moving at {} pace with {} rations
Settlers are in {} health""".format(self.mile, self.day, self.food, self.pace_str(), self.ration_str(), self.group_health())

    def can_move(self):
        """ Returns True if there are any settlers alive, False otherwise
        :return: bool
        """
        if self.alive() == True:
            return True
        else:
            return False

    def arrived(self):
        """ Returns True if they've made it the 2170 miles to Oregon, False otherwise
        :return: bool
        """
        if self.mile >= 2170:
            return True
        return False

    def alive(self):
        """ Returns True if there are settlers alive, False if not
        :return: bool
        """
        for settler in self.settlers:
            if settler.health > 0:
                return True
        return False

    def game_over(self):
        """ Returns True if the game is over.  The game is over if they made it to oregon,
                            or all the settlers are dead.  Otherwise it returns False
        :return: bool
        """
        if self.arrived() == True:
            return True
        if self.alive() == False:
            return True
        if self.food <=0:
            return True
        return False

    def feed_settlers(self):
        """ Decrements the food and feeds the settlers
            If rations is 1, then each settler eats 3 pounds of food / day
            If rations is 2, then each settler eats 2 pounds of food / day
            If rations is 3, then each settler eats 1 pound of food / day
        :return: None
        """
        mult = len(self.settlers)
        if self.rations == 1:
            self.food = self.food - (mult * 3)
        elif self.rations == 2:
            self.food = self.food - (mult * 2)            
        else:
            self.food = self.food - (mult * 1)            

    def adjust_health(self):
        """ Adjusts the health of all the settlers depending on rationing and pace.
            Less food, faster pace depletes their health faster.
            If a settler health is <= 0, then they are dead and removed from the wagon.  RIP

            The amount each settler loses in health is a random number.

                                        pace
                    1           |       2           |       3           |
                ---------------------------------------------------------
    ration  1   | randint(0, 1) |    randint(0, 2)  |   randint(0, 3)   |
            2   | randint(0, 2) |    randint(0, 4)  |   randint(0, 6)   |
            3   | randint(0, 3) |    randint(0, 6)  |   randint(0, 9)   |

        :return: None
        """
        
        mult = self.pace * self.rations
        for settler in self.settlers:
            settler.health -= random.randint(0,mult)
            if settler.health <= 0:
                option = random.randrange(0,len(settler.modes_of_death))
                cause_of_death = settler.modes_of_death[option]
                print("{} died of {}".format(settler.name, cause_of_death))
                self.settlers.remove(settler)

    def move(self):
        """ Moves the wagon by the game rules
            The player only moves if they can move and they haven't arrived yet.
            The number of miles covered if they can is random and dependent on pace
                If the pace is 1, then they move from 5 - 10 miles inclusive
                If the pace is 2, then they move from 13 - 17 miles inclusive
                If the pace is 3, then they move from 18 - 23 miles inclusive
            If they haven't arrived, then you should call feed_settlers and adjust health.
            The day should get incremented.
        :return: None
        """
        if self.game_over() == False:
            if self.pace == 1:
                self.mile += random.randint(5,10)
            elif self.pace == 2:
                self.mile += random.randint(13,17)
            else:
                self.mile += random.randint(18,23)
            if self.arrived() == False:
                self.feed_settlers()
                self.adjust_health()
            self.day += 1
            

    def rest(self, days):
        """ Rests the Group for a given number of days.
            Each day of rests returns back 2 health to each settler.  ( Don't forget to feed them each day )
        :param days: int - How many days to Rest
        :return: None
        """
        for day in range(1,days+1):
            print("Resting day {}".format(day))
            for settler in self.settlers:
                if settler.health <= 98:
                    settler.health += 2
            self.feed_settlers()
            self.adjust_health()

def get_choice(options : str, lower : int, upper : int):
    """Gets choice from user. Validates input based on passed parameters.
    Outputs options menu based on parameter passed
    return: choice:str
    """
    valid = []
    for num in range(lower, upper + 1):
        valid.append(str(num))
    print(options)
    choice = input('==>')
    while choice not in valid:
        print("You must choose from options:", end='')
        for op in valid:
            print(' {}'.format(op), end ='')
        print('\n')
        print(options)
        choice = input('==>')
    return choice

#Menus
main_title = 'Python Trail'
main_menu = """{:^50}

1. Continue on Trail
2. Change Pace
3. Change Rations
4. Rest
5. Settler Report
""".format(main_title)

rations_title = 'Change Rations'
rations_menu = """{:^50}
1. Normal
2. Small
3. Starving
""".format(rations_title)

pace_title = 'Change Pace'
pace_menu = """{:^50}
1.Slow
2.Moderate
3.Fast
""".format(pace_title)

rest_title = 'Rest'
rest_menu = """{:^50}
How many days would you like to rest?
""".format(rest_title)

def play_trail(wagon):
    """ Iterates over trail until they get to the destination or lose """
    
    while not wagon.game_over():

        print(wagon)
        print()
        menu_choice = get_choice(main_menu,1,5) # Get the players choice from menu
        if menu_choice == "1":
            wagon.move()
        elif menu_choice == "2":  # change Pace
            pace_choice = get_choice(pace_menu,1,3) # Get new pace from user
            wagon.pace = int(pace_choice)
        elif menu_choice == "3":  # Change Rations
            ration_choice = get_choice(rations_menu,1,3)# Get new Ration choice from user
            wagon.ration = int(ration_choice)
        elif menu_choice == "4":
            rest_days = int(get_choice(rest_menu,1,10)) # Get number of days to rest from user.
            wagon.rest(rest_days)
        elif menu_choice == "5":  # output the state of the settlers
            print("Settlers ")
            for settler in wagon.settlers:
                print(settler)
        
wagon = Wagon(2000)
wagon.settlers.append( Person("Landon"))
wagon.settlers.append( Person("Cara"))
wagon.settlers.append( Person("Kristopher"))
wagon.settlers.append( Person("Dakota"))
wagon.settlers.append( Person("Jen"))
play_trail(wagon)
