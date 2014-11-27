"""
Name: runningTotal.py
Description: holds running total of string of numbers
Version: 1.0.0
Python: 3.3.5
"""

__author__ = "Spencer Dockham"
__date__ = "10/29/2014"
# DEF

def sumN(tmp):
    total = 0
    for ct in range(1,int(tmp)+1):
        total = total+ct
    return total

# MAIN

#running total
print("runningTotal.py")
number = input("Enter a number: ")
if int(number) < 0:
    print("Number must be zero or greater...")
    number = input("Enter a number: ")
newNumber = sumN(int(number))
# printer
print("Running Total: "+str(newNumber))
    
# program concluded
print("Done")
# pause keeps the command window open
pause = input("Press any key to end: ")
