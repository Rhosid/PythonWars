"""
Name: runningCubedTotal.py
Stuffs: by Spencer and Nick!
Date: 10/29/14

NOTE: returns cubed. Not the running total.. not sure how to do that.
"""
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


