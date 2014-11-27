"""
Name: sumList.py
Description: sums all the digits in the list
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

def addString(string):
    total = 0
    stringList = string.split(" ")
    for ct in range(0,len(stringList)):
        total = total + int(stringList[ct])
    return total

# LISTS
numbet = ['0','1','2','3','4','5',
          '6','7','8','9',' ']

# MAIN

# sum list
print("4sumList.py")

string = input("Please Enter a string of numbers separated by spaces: ")
while checkString(string) == False:
    print("Error.. found none number.")
    string = input("Please Enter a string of numbers separated by spaces: ")
total = addString(string)
print("Total of string: "+str(total))

# program concluded
print("Done")
# pause keeps the command window open
pause = input("Press any key to end: ")
