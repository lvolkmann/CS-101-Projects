########################################################################
## CS 101
## GeneticProgram(LV).py
## Honors Contract
## Landon Volkmann
## lsvr34@mail.umkc.edu
##
## PROBLEM:
##
##  1. Manipulate a randomly generated string into a target string via selective breeding.
##  2. Use classes
##
## ALGORITHM:
##
##  Initalize population of n number of randomly generated members
##      Each member is randomly genrated string of length of TARGET
##      Each member's score is calculated by calculating character distance from TARGET
##  While no member's score is equivalent to 0:
##      Get Average score of the population
##      Get list of above average members of current population and assing to FIT
##      Intialize empty list NEW GENERATION
##      For each count in n:
##          Randomly choose 2 members (MOM, DAD) from FIT
##          Intialize empty string (CHILD)
##          For each place in length of TARGET
##              50% Chance of correspond MOM character given to CHILD
##              50% Chance of correspond DAD character given to CHILD
##              01% Chance of inherited character being incremented(50%)/decremented(50%) by 1
##          Append CHILD to NEW GENERATION
##      Initialize population of n number of members of NEW GENERATION
##
## ERROR HANDLING:
##
##  Performs increasingly poorly as target string length increases and population size decreases.
##      
########################################################################

#Modules

import random

#Classes

class Population(object):
    
    def __init__(self, members = [], target = '', desired_size = 0):
        """Initialize Population. Contatins list of members, worst score, list of fittest members."""
        
        self.members = members
        if len(members) == 0:
            self.create_random_pop(desired_size, target)

        self.worst_score = len(target) * 94
        self.fit_members = self.get_fit_members()

    def create_random_pop(self, desired_size, target):
        """Generates random population of desired size"""
        
        for i in range(desired_size):
            self.members.append( Member(target) )

    def get_best_member(self):
        """Identifies fittest member in population"""

        best_score = self.worst_score
        best_member = None
        
        for member in self.members:
            if member.score < best_score:
                best_score = member.score
                best_member = member
                
        return member

    def get_avg_score(self):
        """Get average score of a population"""
        
        total = 0
        for member in self.members:
            total += member.score
        return total / len(self.members)
    
    def get_fit_members(self):
        """Returns a list of members with an above average fitness score"""
        
        fit_members = []
        avg = self.get_avg_score()
        for member in self.members:
            if member.score <= avg:
                fit_members.append(member)
        return fit_members

    def breed(self, target, desired_size):
        """
Returns list of child members of parents of the fittest members of the current population.
Parents chosen randomly. Child has 50% chance of inheriting from either parent per character position.
1% chance of mutation (incrementing or decrementing by 1 character.
Returns list of members.
    """
        
        new_generation = []
        
        for cnt in range(desired_size):
            mom = self.fit_members[random.randint(0, len(self.fit_members) - 1)]
            dad = self.fit_members[random.randint(0, len(self.fit_members) - 1)]

            child = ''

            for index in range(len(mom.name)):

                #Inherit character from either Mom or Dad
                if random.randint(0,1) == 0:
                    character = mom.name[index]
                else:
                    character = dad.name[index]

                #1% Chance of random mutation
                if random.randint(0,99) == 0:
                    if ord(character) == 126:
                            character = chr(ord(character) - 1)
                    elif ord(character) == 32:
                        character = chr(ord(character) + 1)
                    else:
                        if random.randint(0, 1) == 0:
                            character = chr(ord(character) + 1)
                        else:
                            character = chr(ord(character) - 1)
                            
                child += character
                
            new_generation.append( Member(target, child) )
            
        return new_generation
                    

class Member(object):

    def __init__(self, target = '', member_string = -1):
        """Initalize Member. Contains member name and member score."""

        #Child Member
        if member_string != -1:
            self.name = member_string

        #Random Member
        else:    
            self.name = self.generate_random_name(target)
           
        self.score = self.get_score(target)
        
    def generate_random_name(self, target):
        """Generates Random Member String"""
        
        string = ''
        for char in target:
            string += chr(random.randint(32,126))
        return string
    
    def get_score(self, target):
        """Gets score of given Member"""
        
        fitness_score = 0
        for index, char in enumerate(self.name):
            fitness_score += abs(ord(char) - ord(target[index]))
        return fitness_score

    def __str__(self):
        """Print Member"""

        output = "Member Name: {}\nScore: {}"
        return output.format(self.name, self.score)

#Main Code

#Population Size                       
n = 500

#Target String
target = "Hello Felix, this is a genetic alg in action."

#Inital Population
pop = Population([], target, n)

#Generation Counter
generation = 0

while pop.get_best_member().name != target:

    #Increment Generation Counter
    generation += 1
    print("Generation: {}".format(generation))
    print(pop.get_best_member())

    #Get next generation from fittest members of previous
    new_gen = pop.breed(target, n)
    pop = Population(new_gen, target, n)
    
    print()

#Final Generation
generation += 1
print("Generation: {}".format(generation))
print(pop.get_best_member())

    
