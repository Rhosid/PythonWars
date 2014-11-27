"""
Name: palindrome.py
Stuffs: by Spencer!
Date: 10/29/14
"""


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

# pause keeps the command window open
pause = input("Press any key to end: ")
