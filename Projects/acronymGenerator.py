"""
Name: acronymGenerator.py
Description: generates an acronym out of a sentence
Version: 1.0.1
Python: 3.3.5
"""

__author__ = "Spencer Dockham"
__date__ = "10/20/2014"

# DEF

def acroGen(string):
    string = string.title()
    acro = ""
    for ch in string:
        if ch in capabet:
            acro += ch
    return acro

# LISTS

capabet = ['A','B','C','D','E','F','G','H','I','J',
           'K','L','M','N','O','P','Q','R','S','T',
           'U','V','W','X','Y','Z']

# MAIN

# acronym generator
print("acronymGenerator.py")
string = input("Please Enter String: ")
acro = acroGen(string)
print("Acronym: "+acro)

# program concluded
print("Done")
# pause keeps the command window open
pause = input("Press any key to end: ")
