########################################################################
## CS 101
## HoppersHoagies(LV).py
## Program #1
## Landon Volkmann
## lsvr34@mail.umkc.edu
##
## PROBLEM   : Input number of products(sandwiches) sold and program needs
##             to return how many of each ingredient needed.
##
## ALGORITHM : 
##      1. Prompt for input of sandwich sold
##      2. Multiply number of sandwiches by respective ingredient rates.
##      3. Return sum of products.
## 
## ERROR HANDLING:
##      "Assume the user will enter only valid numeric values."
##      
########################################################################


#Dictionaries containing ingredients required and are organized by sandwich type --> size --> ingredient : amount
italian = {
    'small' : {
        'loaf'   : .5,
        'salami' : .3,
        'veggies': .2,
        'cheese' : 4},
    'large' : {
        'loaf'   : 1,
        'salami' : .5,
        'veggies': .5,
        'cheese' : 8}
    }

vegetarian = {
    'small' : {
        'loaf'   : .5,
        'veggies': .5,
        'cheese' : 5},
    'large' : {
        'loaf'   : 1,
        'veggies': 1.2,
        'cheese' : 11}
    }

tbird = {
    'small' : {
        'loaf'   : .5,
        'turkey' : .4,
        'cheese' : 3},
    'large' : {
        'loaf'   : 1,
        'turkey': .9,
        'cheese' : 8}
    }

#Prompts user to input how many of each kind of sandwich sold
small_ital = int(input("How many small Italians were sold? : ==>"))
large_ital = int(input("How many large Italians were sold? : ==>"))

small_veg = int(input("How many small Vegetarians were sold? : ==>"))
large_veg = int(input("How many large Vegetarians were sold? : ==>"))

small_tbird = int(input("How many small TBirds were sold? : ==>"))
large_tbird = int(input("How many large TBirds were sold? : ==>"))

#Ingredient counting mechanism arranged by sandwich
ital_loaf_total    = (small_ital * italian['small']['loaf']) + (large_ital * italian['large']['loaf'])
ital_salami_total  = (small_ital * italian['small']['salami']) + (large_ital * italian['large']['salami'])
ital_veggies_total = (small_ital * italian['small']['veggies']) + (large_ital * italian['large']['veggies'])
ital_cheese_total  = (small_ital * italian['small']['cheese']) + (large_ital * italian['large']['cheese'])

veg_loaf_total     = (small_veg * vegetarian['small']['loaf']) + (large_veg * vegetarian['large']['loaf'])
veg_veggies_total  = (small_veg * vegetarian['small']['veggies']) + (large_veg * vegetarian['large']['veggies'])
veg_cheese_total   = (small_veg * vegetarian['small']['cheese']) + (large_veg * vegetarian['large']['cheese'])

tbird_loaf_total   = (small_tbird * tbird['small']['loaf']) + (large_tbird * tbird['large']['loaf'])
tbird_turkey_total = (small_tbird * tbird['small']['turkey']) + (large_tbird * tbird['large']['turkey'])
tbird_cheese_total = (small_tbird * tbird['small']['cheese']) + (large_tbird * tbird['large']['cheese'])

#Total summations
loaf_total    = ital_loaf_total + veg_loaf_total + tbird_loaf_total
salami_total  = ital_salami_total
veggies_total = ital_veggies_total + veg_veggies_total
turkey_total  = tbird_turkey_total
cheese_total  = ital_cheese_total + veg_cheese_total + tbird_cheese_total

#Output ingredients required to the tenths place when neccesary
print("You have used:\n%.1f loaves of bread\n%.1f lbs of salami\n%.1f lbs of vegetables\n%.1f lbs of turkey\n%d slices of cheese\nThank you! Come again!"
      % (loaf_total, salami_total, veggies_total, turkey_total, cheese_total))
input()
