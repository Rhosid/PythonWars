"""
Name: 4sumList.py
Stuffs: by Spencer and Nick!
Date: 10/29/14
"""

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


