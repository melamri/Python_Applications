#Ikbel El Amri
#CodeAcademy unit 8 Project
#Command Line Calendar

"""In this project, we'll build a basic calendar that the user will
be able to interact with from the command line. The user should be
able to choose to:
    View the calendar
    Add an event to the calendar
    Update an existing event
    Delete an existing event

The program should behave in the following way:
    Print a welcome message to the user
    Prompt the user to view, add, update, or delete an event on the calendar
    Depending on the user's input: view, add, update, or delete an event on the calendar
    The program should never terminate unless the user decides to exit"""

from time import sleep, strftime
from sys import stdout

def loading(message):
    """display the loading aninmation"""
    stdout.write(message)
    sleep(0.4)
    for i in range(3):
        stdout.write('.')
        sleep(0.2)
    print('.\n')

def get_user_name():
    """prompt the user for their name and return it"""
    #prompt user for their first name
    USER_FIRST_NAME = raw_input("To start, please enter your first name: ")
    #in case entry is invalid (empty) prompt user for their name again
    while USER_FIRST_NAME=="":
        print "\nInvalid entry."
        USER_FIRST_NAME = raw_input("Please enter your first name: ")
    #return name
    return USER_FIRST_NAME

def welcome():
    """displays the initialization messages: welcome message with the user's name"""
    #print the start message
    loading("Starting calendar")
    #prompt user for their name
    NAME = get_user_name()
    #print welcome message using concatenation
    print "\nWelcome to the Calendar App, " + NAME + "!\n"
    sleep(0.75)    #pause program 
    #print current date and time using the imported strftime function
    #documentation: https://docs.python.org/2/library/time.html#time.strftime
    print "Today is: " + strftime("%A %B %d, %Y") + "\n"
    print "The time is: " + strftime("%X") + "\n"
    sleep(0.75)    #pause program
    print "What would you like to do?"

def start_calendar(calendar):
    """calendar functionality"""
    def view():
        """view calendar"""
        loading("\nAccessing calendar") #print animation
        #if calendar is empty
        if len(calendar.keys())<1:
            print "Calendar is empty.\n"
            sleep(1) #sleep program for 1s
        else:
            print calendar

    def update():
        """update calendar"""
        #prompt user for event to update calendar with
        date = raw_input("\nEnter date (MM/DD/YYYY): ")
        while len(date)!=10: #check entry and prompt user again until valid input is entered
            print "\nEntry is invalid." #error message
            date = raw_input("Enter date in this format MM/DD/YYYY (including the slashes): ")
        update = raw_input("Enter the update: ")
        while len(update)<1:
            print "\nEntry is invalid." #error message
            update = raw_input("Enter the update: ")
        #update calendar by adding the update to the date that the user specifies
        calendar[date] = update
        loading("\nUpdating calendar") #print animation
        print "Update successful!\n" #update confirmation
        print calendar
        sleep(1) #sleep program for 1s

    def add():
        """add event to calendar"""
        #prompt user for event to add to calendar
        event = raw_input("\nEnter the event you would like to add: ")
        while len(event)<1:
            print "\nEntry is invalid." #error message
            event = raw_input("Enter the event you would like to add: ")
        date = raw_input("Enter date (MM/DD/YYYY): ")
        while len(date)!=10: #entry validity checker
            print "\nEntry is invalid." #error message
            date = raw_input("Enter date in this format MM/DD/YYYY (including the slashes): ")
        #add event to calendar
        calendar[date] = event
        loading("\nAccessing the calendar") #print animation
        print "Event added successfully!\n" #add confirmation
        print calendar
        print "\n"
        sleep(1) #sleep program for 1s

    def delete():
        """delete event from calendar"""
        loading("\nAccessing calendar events") #print animation
        #if calendar is empty
        if len(calendar.keys())<1:
            print "Calendar is empty. There are no events to delete.\n"
            sleep(1) #sleep program for 1s
        #if events exist inside the calendar
        else:
            event = raw_input ("Which event would you like to delte? ")
            while len(event)<1: #check for errors in the input and prompt again if input is invalid
                print "\nEntry is invalid." #error message
                event = raw_input ("Which event would you like to delte? ")
            #iterate through the dates (keys) and find the matching event (value)
            for date in calendar.keys():
                loading("\nFinding event") #animation
                #if event is found
                if event == calendar[date]: 
                    del calendar[date] #delete event from calendar
                    loading("\nDeleting event") #animation
                    print "Event deleted successfully.\n" #confirm delete
                    sleep(1) #sleep program for 1s
                    #print remaining events in calendar. indicate calendar is empty if no more events exist
                    if len(calendar.keys())<1:
                        print "Calendar is empty."
                        sleep(1) #sleep program for 1s
                    else:
                        print calendar
                        sleep(1) #sleep program for 1s
                    break #skip rest of code in this function
            #if event to delete does not exist inside the calendar
            else:
                print "Could not find the event in the calendar."
                #ask if the user would like to continue with the program
                try_again = raw_input("Try Again? Press Y for Yes if you would like to perform another action, or press N for No to exit: ")
                try_again = try_again.upper()
                while try_again!="Y" and try_again!="N": #check entry and prompt again if invalid
                    print "\nEntry is invalid." #error message
                    try_again = raw_input("Try Again? Y for Yes, N for No: ")
                    try_again = try_again.upper()
                if try_again == "Y": #if user would like to try another action
                    print "\n"
                    return #start loop from the beginning
                elif try_again == "N": #if user chooses to exit program
                    return "Exit" #return exit command

    def leave():
        """exit calendar program"""
        print "\nThank you for using the Calendar App!"
        loading("Exiting program")
        return False   
              
    print "You can view the calendar, update it, add to it or delete from it.\n"
    #we need the project to terminate only when the user voluntarily exits the program
    run_calendar = True
    #prompt user for desired action
    while run_calendar:
        user_choice = raw_input("Please enter A to Add, U to Update, V to View, D to Delete or X to Exit: ")
        user_choice = user_choice.upper()
        #if user enters invalid input
        while user_choice!="A" and user_choice!="U" and user_choice!="V" and user_choice!="D" and user_choice!="X":
            print "\nInvalid entry." #error message
            #prompt user for desired action until entry is valid
            user_choice = raw_input("Please enter A to Add, U to Update, V to View, D to Delete or X to Exit: ")
            user_choice = user_choice.upper()
        
        #user asks to view the calendar
        if user_choice == "V":
            view()
            
        #user asks to update the calendar
        elif user_choice == "U":
            update()
            
        #user asks to add to the calendar
        elif user_choice == "A":
            add()
            
        #user asks to delete an event from the calendar
        elif user_choice == "D":
            command = delete()
            #if delete function returns an exit command
            if command == "Exit":
                run_calendar = leave() #exit program

        elif user_choice == "X":
            run_calendar = leave()
            
    
def main():
    #print welcome messages
    welcome()
    
    #a calendar allows users to at least associate an event with a date, as a pair
    #for this reason, we will use a dictionary as data structure for our calendar
    calendar = {}

    #run the calendar
    start_calendar(calendar)
main()

"""if len(date)<1:
            print "\nEntry is invalid." #error message
            #ask if the user would like to continue with the program
            try_again = raw_input("Try Again? Y for Yes, N for No: ")
            try_again = try_again.upper()
            while try_again!="Y" and try_again!="N": #check entry and prompt again if invalid
                print "\nEntry is invalid." #error message
                try_again = raw_input("Try Again? Y for Yes, N for No: ")
                try_again = try_again.upper()
            if try_again == "Y": #if 
                continue #start loop from the beginning
            else: #if user chooses to exit program
                run_calendar = False"""
