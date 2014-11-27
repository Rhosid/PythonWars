"""
Name: 6reversalInteger.py
Stuffs: by Spencer and Nick!
Date: 10/29/14
"""

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
