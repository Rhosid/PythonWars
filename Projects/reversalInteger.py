"""
Name: reversalInteger.py
Description: reverse all integers in string
Version: 1.0.2
Python: 3.3.5
"""

__author__ = "Spencer Dockham"
__date__ = "10/29/2014"

# DEF
def checkString(string):
    for ch in string:
        if ch not in numbet:
            return False
    return True

def revNumbers(num):
    # extended slice syntax.
    # It works by doing: [begin:end:step]
    # By leaving begin and end off
    # and adding step to -1 it reverses a string
    revNum = num[::-1]
    return revNum

# LISTS
numbet = ['0','1','2','3','4','5',
          '6','7','8','9',]

# MAIN

# reversal integer
print("6reversalInteger.py")
#rfind()
num = input("Please enter a digit greater than 9: ")
while checkString(num) == False:
    print("Error.. found none number.")
    num = input("Please enter a digit greater than 9: ")
revNum = revNumbers(num)
print("Your number reversed: "+str(revNum))

# program concluded
print("Done")
# pause keeps the command window open
pause = input("Press any key to end: ")
