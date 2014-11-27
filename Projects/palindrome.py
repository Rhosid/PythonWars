"""
Name: palindrome.py
Description: askes for a string and checks if palindrome, returns T/F
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

def isPalindrome(num):
    revNum = num[::-1]
    if revNum == num:
        return True
    return False

# LISTS
numbet = ['0','1','2','3','4','5',
          '6','7','8','9',]

# MAIN

# palindrome
print("7palindrome.py")
#rfind()
num = input("Please enter a digit greater than 9: ")
while checkString(num) == False:
    print("Error.. found none number.")
    num = input("Please enter a digit greater than 9: ")
if isPalindrome(num):
    print("You entered a palindrome!")
else:
    print("You did not enter a palindrome.")

# program concluded
print("Done")
# pause keeps the command window open
pause = input("Press any key to end: ")
