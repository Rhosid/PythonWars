"""
Name: runningCubedTotal.py
Description: prints the running total of the cubed numbers
Version: 1.0.0
Python: 3.3.5
"""

__author__ = "Spencer Dockham"
__date__ = "10/29/2014"

# DEF

def sumN(tmp):
    total = 0
    for ct in range(1,int(tmp)+1,1):
        total = total + ct ** 3
    return total

# MAIN

#running total
print("runningCubedTotal.py")
number = input("Enter a number: ")
newNum = sumN(number)
print("Number Cubed: "+str(newNum))

# program concluded
print("Done")
# pause keeps the command window open
pause = input("Press any key to end: ")
