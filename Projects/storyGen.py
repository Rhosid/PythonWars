"""
Name: storyGen.py
Description: creates a story from user input
Version: 1.0.0
Python: 3.3.5
"""

__author__ = "Spencer Dockham"
__date__ = "11/28/2014"

# DEF

def printMenuSubject():
    print("1. Action");print("2. Comedy")
    print("3. Horror")
    tmpChoice = input("Please enter an option: ")
    tmpList = ['1','2','3','4']
    while tmpChoice not in tmpList:
        print("Sorry, please enter a number within range.")
        tmpChoice = input("Please enter an option: ")
    if tmpChoice == '1':
        return "Action"
    elif tmpChoice == '2':
        return "Comedy"
    elif tmpChoice == '3':
        return "Horror"
    else:
        return "Fail"

def printStory(sub,char,name,loc):
    if sub == "Action":
        print("-"*69)
        print("Once there was nothing...")
        print("And then there was "+name+".")
        print(name+" was the strongest warrior in "+loc+".")
        print("But there was one issue... "+name+"'s ego was crushed.")
        print("When "+name+" was young, milk wasn't plentiful in "+loc+".")
        print("Without milk, "+name+", the warrior failed to defeate the dragon.")
        print("...")
        print(name+" the "+char+" died.")
        print("The End")
        print("-"*69)
    if sub == "Comedy":
        print("-"*69)
        print("Once upon a time")
        print(name+", the "+char+", decided to learn how to surf the web.")
        print(name+" traveled from the bottom of vallies to the peak of "+loc+".")
        print("This "+char+" was dedicated to learn the ways of surfing.")
        print("He studied spiders at dawn and watched the water come in at night.")
        print("The waves of the ocean inspired "+name+".")
        print("After months of studying and practice, "+name+" felt prepared.")
        print(name+" was ready to surf the web.")
        print("This dumb "+char+" drowned that night.")
        print("Let it be a lesson to all! Don't let "+char+"'s do anything.")
        print("The End")
        print("-"*69)
    if sub == "Horror":
        print("-"*69)
        print("Long ago in "+loc+", "+name+", the "+char+" died in a tragic accident.")
        print("It scared all of the people in "+loc+".")
        print("We hope that this scared you too...")
        print("The End")
        print("-"*69)      

# MAIN
print("Ready to create a story?")

# choose subject
print("Please choose a subject...")
subject = printMenuSubject()
while subject == "Fail":
    print("ERROR: Failed to read subject.")
    subject = printMenuSubject()

# choose main character
print("EXAMPLE: Human, Turtle, Cat, Plane")
mainChar = input("What is the main character? ")
mainChar = mainChar.title()

# get main character name
charName = input("What is the "+mainChar+"'s name? ")
charName = charName.title()

# get location
loc = input("Where does your story take place? ")
loc = loc.title()

#-----------------------------------
printStory(subject,mainChar,charName,loc)

# program concluded
print("Done")
# pause keeps the command window open
pause = input("Press any key to end: ")




