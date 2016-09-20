#Ikbel El Amri
#CodeAcademy unit 10 project
#Bitwise Operations
#RGB-HEX Converter

"""In this project, we'll use Bitwise operators to build a calculator
that can convert RGB values to Hexadecimal (hex) values, and vice-versa.

The program includes the following methods:
    A method to convert RGB to Hex
    A method to convert Hex to RGB
    A method that starts the prompt cycle

The program performs the following:
    Prompt the user for the type of conversion they want
    Ask the user to input the RGB or Hex value
    Use Bitwise operators and shifting in order to convert the value
    Print the converted value to the user"""

from sys import stdout
from time import sleep

def loading(message, n):
    """display the loading aninmation"""
    stdout.write(message)
    sleep(0.5)
    for i in range(n):
        stdout.write('.')
        sleep(0.2)
    print('.\n')

def rgb_hex():
    """converts RGB to Hex"""
    #information re RGB
    print "\nAn RGB value contains three separate values, with each value\
representing an amount of red (R), green (G), and blue (B).\n\
Acceptable values are within the range of 0 to 255"
    #pause program
    sleep(1)
    
    #constant error message that will display to users when they make an accidental error
    invalid_msg = "\nThe entry is invalid. Acceptable values are within the range of 0 to 255."""
    
    #RGB values input
    #red value input
    red = raw_input("\nTo start, please enter the red (R) value of the RGB color: ") 
    while (not red.isdigit()) or int(red)>255 or int(red)<0: #error checking
        print invalid_msg
        red = raw_input("Please enter the red (R) value: ")
    red = int(red) #convert to integer type
    #green value input
    green = raw_input("\nNext, enter the green (G) value: ") 
    while (not green.isdigit()) or int(green)>255 or int(green)<0: #error checking
        print invalid_msg
        green = raw_input("Please enter the green (G) value: ")
    green = int(green) #convert to integer type
    #blue value input
    blue = raw_input("\nAnd last, enter the blue (B) value: ") 
    while (not blue.isdigit()) or int(blue)>255 or int(blue)<0: #error checking
        print invalid_msg
        blue = raw_input("Please enter the blue (B) value: ")
    blue = int(blue) #convert to integer type

    #A hexadecimal number can be represented with 3 bytes, a byte for each part of R, G, and B.
    #A byte is composed of two nibbles (4 bit numbers). Hexadecimal numbers have 6 characters
    #and each nibble represents a hex character.
    #store sum of shifting red to left by 16 bits, shifting green to left by 8 bits, and blue
    val = (red << 16) + (green << 8) + blue
        #Shifting red to the left by 16 bits will insert 16 bits that will hold the place of green
        #(shifted 8 bits to the left) and blue (no shift).

    #print loading animation
    loading("\nConverting RGB value to HEX", 3)
    
    #Call the hex function and pass the value to it (to represent it in base 16)
    #Use list slicing to print out everything except the first two characters of that string (print in uppercase)
    print "The HEX value is: %s" %(hex(val)[2:].upper())
        #use string formatting to complete all of this in one line of code


def hex_rgb():
    """converts HEX to RGB"""
    #information re HEX
    print "\nValid hexadecimal values are six characters long"
    #pause program
    sleep(1)
    
    #constant error message that will display to users when they make an accidental error
    invalid_msg = "\nThe entry is invalid. Valid hexadecimal values are six characters long."
    
    #HEX value input
    hex_val = raw_input("\nPlease enter the HEX value: ") 
    while len(hex_val)!=6: #error checking
        print invalid_msg
        hex_val = raw_input("Please enter the HEX value: ")
    hex_val = int(hex_val, 16) #convert to integer type
        #The 16 indicates to the int() function that hex_val is in base 16 (a hexadecimal number).

    #initialize value representing two hexadecimal digits
    two_hex_digits = 2**8
    #calculating the RGB values
    #starting from the right, calculating first RGB value: blue (B) value
    blue = hex_val % two_hex_digits
    #shift hex_val to the right by 8 bits
    hex_val = hex_val >> 8
    #calculating green (G) value and shift hex val again
    green = hex_val % two_hex_digits
    hex_val = hex_val >> 8
    #calculating red (R) value
    red = hex_val % two_hex_digits

    #print loading animation
    loading("\nConverting HEX value to RGB", 3)
    
    print "The RGB value is: %s%s%s" %(red,green,blue)
        #use string formatting to complete all of this in one line of code


def convert():
    """starts the prompt cycle"""
    #Welcome message
    print "Welcome to the RGB-HEX Conversion Tool!"
    keep_converting = True
    while keep_converting:
        #prompt user for program starting options
        option = raw_input("\nPlease enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit: ")
        while option.upper()!="X" and option!="1" and option!="2": #error checking
            print("\nInvalid entry.") #error message
            option = raw_input("Please enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit: ")
        #handling user input cases
        #if user enters first option
        if option == "1":
            loading("\nRGB to HEX", 2)
            rgb_hex()
        #if user enters second option
        elif option == "2":
            loading("\nHEX to RGB", 2)
            hex_rgb()
        #if user selects the exit option
        elif option.upper() == "X":
            print "\nThank you for using the RGB-HEX Conversion Tool!"
            loading ("Exiting", 3)
            keep_converting = False

convert()








    
