#Ikbel El Amri
#CodeAcademy Python Unit3 Project

"""Python is especially useful for doing math and can be used to automate many
calculations. In this project, we create a calculator that can compute the
area of a given shape, as selected by the user. The calculator will be able to
determine the area of the following shapes:
    Circle
    Triangle

The program should do the following:
    1. Prompt the user to select a shape
    2. Depending on the shape the user selects, calculate the area of that shape
    3. Print the area of that shape to the user"""

#Since we will calculate the area of a circle, we will need to use the value pi.
from math import pi
#We'll also need access to some more Python code that will be used to simulate a thinking calculator.
from time import sleep
from sys import stdout
#When the program starts, we'll print the date and time to the user.
from datetime import datetime


def loading(message):
    """display the loading aninmation"""
    stdout.write(message)
    sleep(0.5)
    for i in range(4):
        stdout.write('.')
        sleep(0.2)
    print('.\n')

def circle(hint):
    """the part of the program that handles the calculation for the area of a circle"""
    #prompt the user to enter the radius of the circle
    radius = raw_input("\nTo calculate the area of a circle, please enter the radius: ")
    #if user enters invalid input (int or float)
    #i.e. if the radius (string), stripped from up to one period, is all digits
    while not(radius.replace('.','',1).isdigit()):
        #error message and prompt input until it is valid
        print "\nInvalid entry"
        radius = raw_input("Please enter the radius: ")
    #convert radius to float
    radius = float(radius)
    #calculate the area of the circle
    area = pi * radius**2
    #print animation and simulate a thinking calculator
    loading("\nThe pie is baking")
    sleep(1)
    #print the area along with the previously stored hint
    print "\nThe area of the circle is: %.2F. \n%s" %(area,hint)

def triangle(hint):
    """the part of the program that handles the calculation for the area of a triangle"""
    #prompt the user to enter the base of the triangle
    base = raw_input("\nTo calculate the area of a triangle, first enter the base: ")
    #if user enters invalid input (int or float)
    #i.e. if the base (string), stripped from up to one period, is all digits
    while not(base.replace('.','',1).isdigit()):
        #error message and prompt input until it is valid
        print "\nInvalid entry"
        base = raw_input("Please enter the base: ")
    #convert radius to float
    base = float(base)

    height = raw_input("\nAnd finally, please enter the height: ")
    while not(height.replace('.','',1).isdigit()):
        #error message and prompt input until it is valid
        print "\nInvalid entry"
        height = raw_input("Please enter the height: ")
    #convert radius to float
    height = float(height)
    
    #calculate the area of the triangle
    area = (0.5) * base * height
    #print animation and simulate a thinking calculator
    loading("\nUni Bi Tri")
    sleep(1)
    #print the area along with the previously stored hint
    print "\nThe area of the triangle is: %.2F. \n%s" %(area,hint)

    
def user_prompt():
    """user-calculator dialog and prompts"""
    #store message to remind users to use the correct unit
    hint = "Don't forget to include the correct units!\n"
    #prompt user to select the shape for which to calculate the area
    option = raw_input("Enter C for circle or T for triangle: ")
    #if user enters invalid input
    while option.lower()!="c" and option.lower()!="t":
        #print error message and prompt input until it fits the conditional 
        print "\nInvalid entry!"
        option = raw_input("Please enter C for circle or T for triangle: ")
    
    #calculating the area of the selected shape
    #if user selects circle
    if option.lower() == "c":
        #calculate area of circle
        circle(hint)
    #only other possibility at this point is user selected triangle
    else:
        #calculate area of triangle
        triangle(hint)
    
def main():
    #retrieve and store the current date and time
    now = datetime.now()

    #calculator initialization message
    loading("Starting the area calculator")

    #use string formatting to print the current date and time
    print "Local time: %s/%s/%s  %s:%s\n" %(now.month, now.day, now.year, now.hour, now.minute)
    #sleep program for animation purposes
    sleep(1)

    #initiate the calculation process
    play_on = True
    while(play_on):
        user_prompt()
        #pause after finishing a calculation
        sleep(2)
        #prompt user to continue or exit the game
        play_message = raw_input('Would you like to calculate the area of another shape? Press \'Y\' to continue. Press \'N\' to exit: ')
        #prompt user to input a response if it's not valid
        while (play_message.lower()!='n' and play_message.lower()!='y'):
          play_message = raw_input('\nWe could not recognize your answer. Please pess \'Y\' to continue. Press \'N\' to exit: ')
        #exit the game in case user presses 'Y'
        if (play_message.lower() == 'n'):
          play_on = False
        #if user inputs 'Y'
        else:
          print('Let\'s try another shape!')
    print('\nThank you for using the Area Calculator.')
    loading("Exiting")
main()







           
