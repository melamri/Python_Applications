"""The Number Guess Game:
Randomly roll a pair of dice
Add the values of the roll
Ask the user to guess a number
Compare the user's guess to the total value
Decide a winner (the user or the program)
Inform the user who the winner is"""

from random import randint
from time import sleep
from sys import stdout


def loading(message):
    """displaying the loading animation"""
    stdout.write(message)
    sleep(0.5)
    for i in range(4):
        stdout.write('.')
        sleep(0.2)
    print('.\n')
    
def get_user_guess():
  """prompt the user for their guess"""
  #prompt user for guess
  guess = raw_input("\nGuess a number: ")
  #repeat prompt if input is invalid
  while (not guess.isdigit()):
    print("Invalid entry. The input has to be an integer.")
    guess = raw_input("Please enter a valid number: ")
  #convert user guess to int and return it
  return int(guess)

def roll_dice(number_of_sides):
  """function will be used to simulate the rolling of a pair of dice."""
  #simulate the first die roll by generating a random integer between 1 and number_of_sides
  first_roll = randint(1, number_of_sides)
  #simulate the second die roll
  second_roll = randint(1, number_of_sides)
  #calculate the maximum value the program can possibly roll
  max_val = number_of_sides * 2
  #let the user know what the maximum possible value is
  print("\nThe maximum possible total value of the dice rolls is " +str(max_val) + ".")
  #sleep the program for 1 second
  sleep(1)
  #prompt the user for their guess
  user_guess = get_user_guess()
  #if the user guesses a number that is larger than the total possible value of the dice roll
  #keep inputting a guess until the entry is no longer invalid
  while user_guess>max_val:
    print("Your guess is larger than the total possible value of the dice roll.")
    user_guess = get_user_guess()
  else:
    #rolling effects
    loading("\nRolling")
    sleep(0.5)
    #announce first die roll
    print("The first die roll reads.. %d" % (first_roll))
    sleep(1)
    #announce second die roll
    print("The second die roll reads.. %d" % (second_roll))
    sleep(1)
    #sum the first and second die rolls
    total_roll = first_roll + second_roll
    #announce the roll
    print("The total roll is %d\n" % (total_roll))
    #result effects
    loading("Result")
    sleep(0.5)
    #announce winner
    if user_guess>total_roll:
      print("It looks like the computer won this round! You guessed a number bigger than the total roll.\
 \nDon't give up. Try again!\n")
    if user_guess==total_roll:
      print("Congrats! You guessed the right number.\
 You are the winner!\n")
    else: 
      print("It looks like the computer won this round! You guessed a number smaller than the total roll.\
 \nDon't give up. Try again!\n")

def main():
  #Welcome message
  print("Welcome to the Number Guess game!\n")
  sleep(1)
  #game description
  print("In this game, we will roll a pair of dice and ask you to guess a number.\
 Based on your guess, the program should determine a winner.\
 If you guess the exact total value of the dice roll, you win!\
 Otherwise, the computer wins.\n")
  sleep(1.5)
  play_on = True
  while(play_on):
    #prompt user for number of sides on each die
    number_of_sides = raw_input("Let's start by specifying the number of sides on each die.\
 But remember, the higher the number of sides, the harder it gets!\
 Enter the number of sides each dice has: ")
    while (not number_of_sides.isdigit()):
      print("Invalid entry. The input has to be an integer.")
      number_of_sides = raw_input("Please enter the number of sides of the dice: ")
    #roll the dice
    roll_dice(int(number_of_sides))
    sleep(1.5)
    #prompt user to continue or exit the game
    play_message = raw_input('Would you like to play another round? Press \'Y\' to play on. Press \'N\' to exit: ')
    #prompt user to input a response if it's not valid
    while (play_message.lower()!='n' and play_message.lower()!='y'):
      play_message = raw_input('\nWe could not recognize your answer. Please pess \'Y\' to play on. Press \'N\' to exit: ')
    #exit the game in case user presses 'Y'
    if (play_message.lower() == 'n'):
      play_on = False
    #if user inputs 'Y'
    else:
      print('Let\'s try another roll!')
  print('\nThank you for playing the Number Guessing game.\nSee you next time!')
   
main()
