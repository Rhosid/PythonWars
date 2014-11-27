"""
Name: distFromMax.py
Description: finds the distance from max
Version: 1
"""

__author__ = "Spencer Dockham"
__date__ = "11/24/2014"

# def
def distFromMax(numList):
    returnList = []
    listLen = len(numList)
    maxNum = max(numList)
    for ct in range(0,len(numList)):
        returnList.append(maxNum - numList[ct])
    return returnList

# main        
numList = []
length = input("Please enter the index of your list: ")
for ct in range(0,int(length)):
    numList.append(int(input(str(ct+1)+" - Please enter a number: ")))
returnList = distFromMax(numList)
for ct in range(0,len(returnList)):
    print("Distance from "+str(numList[ct])+" to "+str(max(numList))+": "+str(returnList[ct]))

# pause program
pause = input("Press any button to Exit...")
