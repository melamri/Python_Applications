#Ikbel El Amri
#CodeAcademy Python Unit3 Project

"""Ask the user to input a word in English.
Make sure the user entered a valid word.
Convert the word from English to Pig Latin.
Display the translation result."""

import sys
import time


#Display the loading aninmation
def loading():
    for i in range(5):
        sys.stdout.write('.')
        time.sleep(0.2)
    print('.')

#translate the valid inputted word into PygLatin
def translate(original):
    #storing the PygLatin suffix
    pyg = 'ay'
    #lowercase the word
    word = original.lower()
    #extract the first letter of the word
    first = word[0]
    #structure the pyg latin outcome
    new_word = word + first + pyg
    #slice the resulting word to remove the first letter
    new_word = new_word[1:len(new_word)]
    return(new_word)

def play_game():
    #inputting a word from the user
    original = raw_input('\nPlease enter a word to translate: ')
    #prompt the user to input the word again until it consists of a valid word 
    #and does not contain any non-alphabetical characters
    while (len(original) == 0) or (not original.isalpha()):
        #display the loading animation
        loading()
        print('The input entered does not appear to be a valid word')
        original = raw_input('\nPlease enter a valid word with no numerals or special characters: ')

    #display loading animation
    loading()
    #translation work
    translated = translate(original)
    #print our PygLatin-translated word
    print('In PygLatin, '+original+' translates to '+translated+'!')
    
def main():
    #welcome message
    print('Welcome to the PygLatin language game!')
    print('Pig Latin is a language game, where you move the first letter of the word \
to the end and add "ay."\ So "Python" becomes "ythonpay."')
    play_on = True
    while (play_on):
        #play the PygLatin game
        play_game()
        #prompt user to continue or exit the game
        play_message = raw_input('\nWould you like to translate another word? Press \'Y\' to play on. Press \'N\' to exit: ')
        #prompt user to input a response if it's not valid
        while (play_message.lower()!='n' and play_message.lower()!='y'):
            play_message = raw_input('\nWe could not recognize your answer. Please pess \'Y\' to play on. Press \'N\' to exit: ')
        #exit the game in case user presses 'Y'
        if (play_message.lower() == 'n'):
            play_on = False
        #if user inputs 'Y'
        else:
            print('Let\'s try another word!')
    print('\nThank you for playing the PygLatin language game.\nSee you next time!')
            

main()
