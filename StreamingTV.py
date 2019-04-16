########################################################################
## CS 101
## StreamingTV(LV).py
## Program #6
## Landon Volkmann
## lsvr34@mail.umkc.edu
##
## PROBLEM   :
##  1. Prompt user to use one of two services
##  2. Implement Service
##      2a. Get price per channel of all TV services based on existing CSV File
##      OR
##      2b. Get price per channel of all TV services based on existing CSV File and
##          show preferences given by user.
##  3. Loop until prompted to quit
##
## ALGORITHM :
##
##  -Incredibly Pythonic due to the fact this is just a formatting program-
##
##  def read_csv(name):
##      lst = []
##      with open(name, "r") as fh:
##          for ln in fh:
##          sep = ln.split(',')
##          stripped = []
##          for item in sep:
##              stripped.append(item.strip())
##      lst.append(stripped)
##      fh.close()
##      return lst
##  
##  def populate_channel_show_dict(lst):
##      dictionary = {}
##     for item in lst:
##          if item[1] in dictionary:
##          dictionary[item[1]].append(item[0])
##          else:
##          dictionary[item[1]] = [item[0]]
##      return dictionary
##  
##  def populate_show_channel_dict(lst):
##      dictionary = {}
##     for item in lst:
##          dictionary[item[0]] = item[1]
##      return dictionary
##  
##  def populate_providers_dict(lst):
##      dictionary = {}
##      for item in lst:
##         channels = read_csv(item[1])
##          ch_lst = []
##          for lst in channels:
##          for ch in lst:
##              ch_lst.append(ch)
##          dictionary[item[0]] = [ch_lst, item[2]]
##      return dictionary
##  
##  def populate_shows_lst(dic):
##      lst = []
##      vals_ch_lst = dic.values()
##      for ch in vals_ch_lst:
##          for val in ch:
##          lst.append(val)
##      return lst
##  
##  def populate_usr_pref_dict(lst,shows):
##      dictionary = {}
##      not_found = []
##      for item in lst:
##          if item[0] in shows:
##          dictionary[item[0]] = int(item[1])
##          else:
##          not_found.append(item[0])
##  return dictionary, not_found
##  
##  def calc_cpc(dic, key):
##      cpc = float(dic[key][1])/ len(dic[key][0])
##      return cpc
##  
##  def calc_points(serv_dict, serv_key, pref_dict):
##      points = 0
##          for channel in serv_dict[serv_key][0]:
##              if channel in ch_interest_dict:
##                  points += int(ch_interest_dict[channel])
##      return points
##
## ERROR HANDLING:
##  1. Divide cost by zero points for cost per point defaults to 10000
##  2. On menu, prompts user until valid input given
##  3. For preference file, prompts user until openable file given
##
########################################################################

#Modules
import csv

#Functions
def menu(valid_ops : list):
    """Pass in valid choice options. Displays menu and prompts user until valid choice given"""
    
    print()
    print("{:^100}".format(menu_title))
    print("{}".format(menu_ops))
    while True:
        choice = input("==>")
        if choice in valid_ops:
            return choice
        print("You must choose a value from 1,2,Q")

def read_csv(name : str):
    """Pass in name of file. Returns list of lists"""
    
    lst = []
    with open(name, "r") as fh:
        for ln in fh:
            sep = ln.split(',')
            stripped = []
            for item in sep:
                stripped.append(item.strip())
            lst.append(stripped)
        fh.close()
        return lst
    
def populate_channel_show_dict(channel_show_lst : list):
    """Pass in list of lists [show, channel]. Returns dictionary with channel as key and list of shows as value"""
    
    dictionary = {}
    for item in channel_show_lst:
        if item[1] in dictionary:
            dictionary[item[1]].append(item[0])
        else:
            dictionary[item[1]] = [item[0]]
    return dictionary

def populate_show_channel_dict(channel_show_lst : list):
    """Pass in list of lists [show, channel]. Returns dictionary with show as key and channel as value"""
    
    dictionary = {}
    for item in channel_show_lst:
        dictionary[item[0]] = item[1]
    return dictionary

def populate_providers_dict(provider_lst: list, read_func):
    """
Pass in lists of lists [provider,file,cost]. Reads file and populates list of channels.
Returns dictionary with provider as key and list [channel list, cost] as value
"""
    
    dictionary = {}
    for row in provider_lst:
        channels = read_func(row[1])
        ch_lst = []
        for lst in channels:
            for ch in lst:
                ch_lst.append(ch)
        dictionary[row[0]] = [ch_lst, row[2]]
    return dictionary

def populate_shows_lst(ch_show_dict : dict):
    """Pass in dictionary {ch:shows}. Returns list of shows"""
    
    lst = []
    vals_ch_lst = ch_show_dict.values()
    for ch in vals_ch_lst:
        for val in ch:
            lst.append(val)
    return lst

def populate_usr_pref_dict(user_pref_lst : list, shows : list):
    """
Pass in list of user preferences [show, rating] and list of shows.
Return dictionary with show as key and rating as value and list of shows not found.
"""
    
    dictionary = {}
    not_found = []
    for row in user_pref_lst:
        if row[0] in shows:
            dictionary[row[0]] = int(row[1])
        else:
            not_found.append(row[0])
    return dictionary, not_found

def calc_cpc(providers : dict, key):
    """Pass in dictionary {provider : [channel list, cost]}. Return cost per channel."""
    cpc = float(providers[key][1])/ len(providers[key][0])
    return cpc

def find_ch_interest_dict(show_channel_dict : dict, usr_pref_dict : dict):
    """Pass in show_channel_dict {show:channels} and usr_pref_dict {show: rating}. Returns dictionary {channel : total rating}"""
    ch_interest_dict = {}
    for show in usr_pref_dict:
        if show in show_channel_dict:
            if show_channel_dict[show] in ch_interest_dict:
                ch_interest_dict[show_channel_dict[show]] += usr_pref_dict[show]
            else:
                ch_interest_dict[show_channel_dict[show]] = usr_pref_dict[show]
    return ch_interest_dict

def calc_points(serv_dict : dict, serv_key, pref_dict : dict):
    """
Pass in providers dictionary {provider : [channel list, cost]},
provider in quesiton, and preference dictionary{show: rating}. Returns points for given provider.
"""
    
    points = 0
    
    for channel in serv_dict[serv_key][0]:
        if channel in ch_interest_dict:
            points += int(ch_interest_dict[channel])
            
    return points

def get_user_pref(read_func):
    """Pass in read csv function. Prompt for file name. Return file data if found."""
    
    while True:
        try:
            usr_pref = input("Enter a file name!")
            usr_pref_data = read_func(usr_pref)
            return usr_pref_data
        except:
            print("Could not open {}. Try another".format(usr_pref))
            
#Menu
menu_title = "Streaming Service Comparison"
menu_ops = """1. Get Price per channel for all services
2. Get Weighted comparison for user file.
Q. Quit"""
valid_ops = ['1','2','q','Q']
 
#Base Data Files
show_ch_file = "shows_channel.csv"
providers_file = "providers.csv"

#Populate Channel Shows Dictionary & Channel List
show_ch_data = read_csv(show_ch_file)
channel_show_dict = populate_channel_show_dict(show_ch_data)
shows_lst = populate_shows_lst(channel_show_dict)

#Populate Show Channel Dictionary
show_channel_dict = populate_show_channel_dict(show_ch_data)

#Populate Providers Dictionary
providers_data = read_csv(providers_file)
providers_dict = populate_providers_dict(providers_data, read_csv)

#Calculate CPP & Make Data Sortable
main_cpc_lst = []
for key in providers_dict:
    cpc = calc_cpc(providers_dict, key)
    ch_cnt = len(providers_dict[key][0])
    price = float(providers_dict[key][1])
    main_cpc_lst.append([cpc, key, ch_cnt, price])
main_cpc_lst.sort()

#Main will loop until user quits
running = True
while running:

    #menu
    service = menu(valid_ops)

    #Cost Per Channel Service
    if service == "1":
        
        #Output Cost Per Channel Summary
        print("{:^100}".format("Cost per Channel Summary"))
        print("{:<40}{:<20}{:<20}{:<20}".format("Service", "CPC", "Channels", "TTL Price"))
        print("="*100)
        for entry in main_cpc_lst:
            print("{:<40}${:<20.4f}{:<20}${:<20}".format(entry[1], entry[0], entry[2], entry[3]))

        print()
        input("Hit enter to continue")

    #Cost Per Point Service 
    elif service == "2":
        usr_pref_data = get_user_pref(read_csv)
        usr_pref_dict, not_found = populate_usr_pref_dict(usr_pref_data, shows_lst)

        ch_interest_dict = find_ch_interest_dict(show_channel_dict, usr_pref_dict)

        #List of list to be sorted by cpp
        main_cpp_lst = []

        #Generates list of cpp, points, and price for each provider
        for key in providers_dict:

            #Calculates points for provider
            points = calc_points(providers_dict, key, usr_pref_dict)
            price =float(providers_dict[key][1])

            #Calculate cost per point
            try:
                cpp = price/points
                
            #CPP = 10000 if no points for given provider
            except ZeroDivisionError:
                cpp = 10000

            #Append data to list with CPP as leading value
            main_cpp_lst.append([cpp, key, points, price])

        #Sort by CPP
        main_cpp_lst.sort()
            
        #Output Cost Per Point Summary
        print("Could not find: ", end='')
        for show in not_found:
            print("{} ".format(show), end = '')
        print()
        print()
        print("{:^100}".format("Cost per Point Summary"))
        print("{:<40}{:<20}{:<20}{:<20}".format("Service", "CPP", "Points", "TTL Price"))
        print("="*100)
        for entry in main_cpp_lst:
            print("{:<40}${:<20.4f}{:<20}${:<20}".format(entry[1], entry[0], entry[2], entry[3]))

        print()
        input("Hit enter to continue")

    #User prompts to quit    
    else:
        running = False
