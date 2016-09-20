#Ikbel El Amri
#Codeacademy unit 5 project

"""In this project, we build Rock-Paper-Scissors!

The program performs the following tasks:

Prompt the user to select either Rock, Paper, or Scissors
Instruct the computer to randomly select either Rock, Paper, or Scissors
Compare the user's choice and the computer's choice
Determine a winner (the user or the computer)
Inform the user who the winner is"""

from random import randint
from time import sleep
from sys import stdout

def loading(message):
    """display the loading aninmation"""
    stdout.write(message)
    sleep(0.5)
    for i in range(4):
        stdout.write('.')
        sleep(0.2)
    print('.\n')
    
def decide_winner(user_choice, computer_choice, options):
    """decide whether the user or the computer wins"""
    #storing win/lose messages
    #(typed in "snake case" as the variables store constant information)
    WIN_MESSAGE = "You won! Congratulations :)\n"
    LOSS_MESSAGE = "You lost!\nDon't give up, try again!\n"
    
    #print user selection
    print "You slected: %s\n" %(user_choice)
    #loading message and animation
    loading("Computer selecting")
    sleep(1)
    #print computer selection
    print "The computer slected: %s\n" %(computer_choice)
    sleep(1)

    #set the user choice index equal to the result of calling
    #the index() function on the options list
    user_choice_index = options.index(user_choice)
    #set the index of the computer's choice
    computer_choice_index = options.index(computer_choice)

    #the rules that determine the winner:
    #in case of a tie
    if user_choice_index == computer_choice_index:
        print("It's a tie!\nDon't give up, try again!")
    #if the user wins. Scenarios:
    #User: Rock, Computer: Scissors
    elif (user_choice_index == 0 and computer_choice_index == 2):
        print WIN_MESSAGE
    #User: Paper, Computer: Rock
    elif (user_choice_index == 1 and computer_choice_index == 0):
        print WIN_MESSAGE
    #User: Scissors, Computer: Paper
    elif (user_choice_index == 2 and computer_choice_index == 1):
        print WIN_MESSAGE
    else:
        print LOSS_MESSAGE

def play_RPS():
    """starts the game"""
    #storing the game options (Rock Paper, or Scissors) in a list
    options = ["Rock", "Paper", "Scissors"]
    
    #welcome message
    print "Welcome to the Rock-Paper-Scissors game!\n"
    #prompt user for their selection
    user_input = raw_input("To start, please select R for Rock, P for Paper, or S for Scissors: ")
    #check for input validity and prompt user for input again if entry is invalid
    while (user_input.lower()!="r" and user_input.lower()!="p" and user_input.lower()!="s"):
        #print error message and prompt user for input again
        print "Invalid entry!\n"
        user_input = raw_input("Please select R for Rock, P for Paper, or S for Scissors: ")
    #sleep program
    sleep(1)
    #convert user_choice to their matching options
    user_input = user_input.upper()
    user_choice = ""
    if user_input == "R":
        user_choice = "Rock";
    elif user_input == "P":
        user_choice = "Paper";
    else:
        user_choice = "Scissors";

    #selecting the choice of the computer (at random)
    computer_choice = options[randint(0,len(options)-1)]

    #decide a winner
    decide_winner(user_choice, computer_choice, options)
    
def main():
    #play the game
    play_on = True
    while(play_on):
        play_RPS()
        #pause after finishing a calculation
        sleep(2)
        #prompt user to continue or exit the game
        play_message = raw_input('Would you like to play another round? Press \'Y\' to continue playing. Press \'N\' to exit: ')
        #prompt user to input a response if it's not valid
        while (play_message.lower()!='n' and play_message.lower()!='y'):
          play_message = raw_input('\nWe could not recognize your answer. Please pess \'Y\' to play again. Press \'N\' to exit: ')
        #exit the game in case user presses 'Y'
        if (play_message.lower() == 'n'):
          play_on = False
        #if user inputs 'Y'
        else:
          print('Let\'s play another round!')
    print('\nThank you for playing the Rock-Paper-Scissors game!')
    loading("Exiting")    

main()
