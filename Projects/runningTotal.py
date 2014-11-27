"""
Name: runningTotal.py
Stuffs: by Spencer and Nick!
Date: 10/29/14
"""
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
