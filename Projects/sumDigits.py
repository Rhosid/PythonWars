"""
Name: sumDigits.py
Description: sum up digits from string
Version: 1.0.0
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

def addN(string):
    total = 0
    for ct in range(0,int(string)+1):
        total = total + ct
    return total

# LISTS
numbet = ['0','1','2','3','4','5',
          '6','7','8','9',' ']

# MAIN

# sum digits
print("5sumDigits.py")

string = input("Please Enter a numbers: ")
while checkString(string) == False:
    print("Error.. found none number.")
    string = input("Please Enter a numbers: ")
total = addN(string)
print("Total of string: "+str(total))

# program concluded
print("Done")
# pause keeps the command window open
pause = input("Press any key to end: ")
