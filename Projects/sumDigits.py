"""
Name: 5sumDigits.py
Stuffs: by Spencer and Nick!
Date: 10/29/14
"""

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
