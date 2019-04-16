########################################################################
## CS 101
## GeneticProgram(LV).py
## Honors Contract
## Landon Volkmann
## lsvr34@mail.umkc.edu
##
## PROBLEM   :
##
## ALGORITHM :  
## 
## ERROR HANDLING:
##      
########################################################################

import random

#Initialize Environment        
pop_size = 500
target = "Hello World. This is how a genetic algorithm works."
gene_size = len(target)
worst_match_value = gene_size * 94

#Initialize Starting Population
population = []
for num in range(0, pop_size):
    string = ''
    for place in range(gene_size):
        string += chr(random.randint(32,126))
    population.append(string)

best_fit = ""

generation = 1
print(generation)

while best_fit != target:
    
    best_score = worst_match_value
    scores = []
    for member in population:
        match_value = 0
        for index, char in enumerate(member):
            #if char == target[index]:
            #    pass
            #else:
            #    match_value += 1
            match_value += abs(ord(char) - ord(target[index]))
        scores.append(match_value)
        if match_value < best_score:
            best_fit = member
            best_score = match_value
    
    print(best_fit)
    avg_score = sum(scores) / len(scores)
    best_members = []
    for index, item in enumerate(population):
        if scores[index] <= avg_score:
            best_members.append(item)

    population = []
    generation += 1
    print(generation)
    
    for num in range(pop_size):
        
        mom = best_members[random.randint(0, len(best_members) - 1)]
        dad = best_members[random.randint(0, len(best_members) - 1)]

        new_member = ""

        for index in range(len(mom)):
            if random.randint(0,1) == 0:
                character = mom[index]
            else:
                character = dad[index]
            
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
                    
            new_member += character
                    
        population.append(new_member)
