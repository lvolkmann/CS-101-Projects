########################################################################
## CS 101
## EmailScraper(LV).py
## Program #4
## Landon Volkmann
## lsvr34@mail.umkc.edu
##
## PROBLEM   :
##
##    1. Get file containing urls on each line
##    2. Search given url html for emails
##    3. Store found emails
##    4. Decoded html encoded emails
##    5. Elimnate duplicate emails
##    6. Output final email list to user named file
##
## Algorithm :
##
##    1.	Givens
##        1.1.	Create list of valid email endings named: endings
##        1.1.1.	Ex. ['.com','.edu','.org','.gov', etc…]
##    2.	Get File
##        2.1.	Create empty list: url_list
##        2.2.	Prompt user for valid file name (& pathway if not in same directory) and assign to file
##        2.2.1.	Continue to prompt until valid
##        2.3.	Open file
##        2.4.	For each line in file
##        2.4.1.	Append line to url_list
##        2.5.	Close file
##    3.	Get Data
##        3.1.	Create empty list: html_list
##        3.2.	For each url in url_list
##        3.2.1.	Assign the result of requesting url to request
##        3.2.2.	Assign the result of opening request to response
##        3.2.3.	Assign the result of reading response to page_data
##        3.2.4.	Assign the result of decoding page_data via utf-8 to page_str
##        3.2.5.	Append page_str to html_lst
##        3.2.6.	Close response
##    4.	Get Emails
##        4.1.	Create empty list: email_lst
##        4.2.	For each string in email_lst
##        4.2.1.	Set total equal to the count of ‘mailto:’s in string
##        4.2.2.	Set count equal to 0
##        4.2.3.	Set starting equal to -1
##        4.2.4.	While count is less than total
##        4.2.4.1.	Set starting equal to the index of the first ‘mailto:’ from position starting + 1
##        4.2.4.2.	Create empty list: candidates_pos
##        4.2.4.3.	Create empty list: candidates_name
##        4.2.4.4.	For each end in endings
##        4.2.4.4.1.	If the index of the first end from position starting is greater than 0
##        4.2.4.4.1.1.	Append index of end to candidates_pos
##        4.2.4.4.1.2.	Append end to candidates_name
##        4.2.4.5.	Assign the smallest integer in candidates_pos to ending
##        4.2.4.6.	Assign the concatenation of string from index (starting+7) to ending and the item at the index of the index ending in candidates_pos in candidates_name to current_email
##        4.2.4.7.	Add 1 to count
##    5.	Output
##        5.1.	Output each item in email_lst
##
## Error Handling:
##
##    Getting File (loops)
##        FileNotFoundError
##        IOError
##        PermissionError
##    Getting Data (skips)
##        HTTPError    
##        ValueError
##    Writing File (skips)
##        Error
##    Running Again (loops)
##        Check for valid input
##
#########################################################################

#Import module
import urllib.request

#Functions
def get_file():
    """
Prompts user for a file name in same directory
Opens and reads file line by line
Closes file
Returns list of urls
Repeats until user provides valid file
"""
    url_list = []

    while True:
        try:
            file_name = input("Enter file name: ")
            file_found = open(file_name, 'r')
            for line in file_found:
                url_list.append(line.strip())
            file_found.close
            
            return url_list
        
        except FileNotFoundError:
            print("We're having trouble opening your file")
            print('File not Found... Dummy')
        except IOError:
            print("We're having trouble opening your file")
            print('IOError')
        except OSError:
            print("We're having trouble opening your file")
            print("That's not even a valid entry... Dummy")
        except PermissionError:
            print("We're having trouble opening your file")
            print("We don't have permission to open that one")
        except:
            print("We're having trouble opening your file")

            

def data_get(url : str):  
    """
Pass url <str>
Requests and reads the response of the url passed
Decodes using utf-8
Reurns page html
"""

    while True:
        
        try:
            request = urllib.request.Request(url)
            response = urllib.request.urlopen(request)
            page_data = response.read()
            page_str = page_data.decode('utf-8')
            response.close()
            return page_str
        
        except urllib.error.HTTPError:
            return False
        
        except ValueError:
            return False

        except:
            return False


    
def get_emails(data: list):
    """
Pass a list
Iterates over each url in list
Finds emails using 'mailto:' and ending quotation mark as endpoints
returns list of emails
"""
    
    while True:
        emails_lst = []
        for string in data:
            total = string.count('mailto:')
            count = 0
            starting = -1
            while count < total:
                
                starting = string.find('mailto:', (starting + 1))
                ending  = string.find('"', starting)
                
                current_email = string[(starting+7):ending]
                
                emails_lst.append(current_email)
                count += 1
                
        return emails_lst
                    
def decrypt (lst: list):
    """
Decodes html encoded emails
Pass a list of emails
Decodes email if starting characters are '&#'
Returns list of unencoded emails
"""
    
    while True:
        unencoded_emails = []
        for string in lst:
            if string[0:2] == '&#':
                slices = int(len(string) / 6)
                count = 0
                starting_pos = 0
                decoded_email = ''
                while count < slices:
                    decoded_email = decoded_email + chr(int(string[starting_pos + 2: starting_pos + 5]))
                    count += 1
                    starting_pos += 6
                unencoded_emails.append(decoded_email)
            else:
                unencoded_emails.append(string)
        return unencoded_emails

            
def write_file(file_name : str , lst : list):
    """
WARNING: Will overwrite existing file
"""
    
    try:
        open_file = open(file_name, 'w')
        for string in lst:
            open_file.write(string)
            open_file.write('\n')
        open_file.close
        
    except:
        print("Something has gone terribly wrong.")

def run_again():
    """
Asks user if would like to run again
Return response
"""
    
    while True:
        
        valid = ['YES', 'Y', 'YEAH', 'NO', 'N', 'NAH']
        
        running = input("Would you like to keep scraping? (Y/YES/N/NO)").upper()

        if running in valid:
            return running
        else:
            print("Error: Please enter Valid Response")


#Main Code
            
running = 'YES'
aff = ['YES', 'Y', 'YEAH']

#Code will run until prompted otherwise
while running in aff:

    #Gets, opens, reads, and closes file
    urls = get_file()

    #Lists to be populated with email addresses
    data_lst = []
    bad_urls = []

    print("Processing...")

    #Gets urls from file
    for add in urls:
        if data_get(add):
            data_lst.append(data_get(add))          
        else:
            print("Failed to read {}".format(add))
            bad_urls.append(add)

    #Gets emails from each url
    emails_lst = get_emails(data_lst)

    #Eliminates duplicates
    unique_emails = set(emails_lst)
    emails_lst = list(unique_emails)

    #Decodes html encoded emails
    decoded_email_lst = decrypt(emails_lst)
    decoded_email_lst.sort()

    #Checks to see if any emails found
    if len(decoded_email_lst) > 0:

        #Write emails to a file of users choice (will overwrite existing file)
        usr_write = input('Enter a file you would like to output to (will overwrite existing file):')
        write_file(usr_write, decoded_email_lst)
        
    else:
        print("Couldn't find any emails to save")

    #Asks user if they want to run program again
    aff = ['YES', 'Y', 'YEAH']
    neg = ['NO', 'N', 'NAH']
    running = run_again()


