#Ikbel El Amri
#CodeAcademy Unit 2 Project
#MadLibs Story

"""In this project, we use Python to write a Mad Libs story!
Mad Libs are stories with blank spaces that a reader can fill in
with their own words. The result is usually a funny (or strange) story.

Mad Libs require:
    Words from the reader (for the blank spaces)
    A story to plug the words into.

The program does the following:
    Prompt the user for input
    Print the entire Mad Libs story with the user's input"""

from time import sleep


def entry(msg):
    """prompt user for input"""
    data = raw_input("Enter " + msg + ": ")
    #error checking
    while data == "":
        print "\nInvalid input." #error message
        #prompt user for input again
        data = raw_input("Please enter " + msg + ": ")
    return data        
    

def main():
    """main method"""
    
    print "Mad Libs is starting!\n" #starting message

    #prompt user for name
    name = entry("your name")

    #input 3 adjs
    adj1 = entry("an adjective")
    adj2 = entry("a second adjective")
    adj3 = entry("a third adjective")

    #input 3 verbs
    verb1 = entry("a verb")
    verb2 = entry("a second verb")
    verb3 = entry("a third verb")

    #input 4 nouns
    noun1 = entry("a noun")
    noun2 = entry("a second noun")
    noun3 = entry("a third noun")
    noun4 = entry("a fourth noun")

    #input remaining words
    animal = entry("an animal")
    food = entry("a food")
    fruit = entry("a fruit")
    number = entry("a number")
    superhero = entry("a superhero name")
    country = entry("a country")
    dessert = entry("a dessert")
    year = entry("a year")

    #user message
    print "\nInput complete."
    print "\nPreparing your story",
    #loadinganimation
    sleep(0.4)
    for i in range(5):
        print("."),
        sleep(0.4)
    print(".\n\n")
    sleep(1)

    #story to be filled by user
    STORY = "This morning I woke up and felt %s because %s was going to finally \
%s over the big %s %s. On the other side of the %s were many %ss protesting to keep \
%s in stores. The crowd began to %s to the rythym of the %s, which made all of the \
%ss very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s\
quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into \
a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where \
%ss ruled the world."

    #printing story formatted with input from user
    print STORY % (adj1, name, verb1, adj2, noun1, noun2, animal, food, verb2, noun3, fruit, adj3, name, verb3, number, name, superhero, superhero, name, country, name, dessert, name, year, noun4)

main()

