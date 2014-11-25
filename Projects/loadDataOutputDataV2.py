"""
Name: loadDataOutputDataV2.py
Description: loads data, calcs grosspay, saves data
Version: 1.0.2
Python: 3.3.5
"""

__author__ = "Spencer Dockham"
__date__ = "11/18/2014"

# DEF
# loadData() reads file and appends to list then returns list
def loadData(fileName):
    # pre: fileName must exist
    # returns tmpList full with empLists
    # tmpList stores list of emps to be returned
    tmpList = []
    # open fileName and assign to myFile
    myFile = open(fileName+".txt",'r')
    # read myFile and assign to data
    data = myFile.read()
    # split data on '\n' and assign to lineList
    lineList = data.split('\n')
    # do loop for each line in linelist
    for line in lineList:
        # assign the line splitting on spaces to wordList
        wordList = line.split(' ')
        # tmpEmp will hold employee info to be appended to tmpList
        tmpEmp = []
        # do loop for each word in wordList
        for word in wordList:
            # append each word to tmpEmp
            tmpEmp.append(word)
        # append the tmpEmp to tmpList
        tmpList.append(tmpEmp)
    # return full list of employees in database
    return tmpList
    # post: none

# calcPay() reads library and calculates pay for each user
def calcPay(lib):
    # pre: library must exist and be populated
    # payLib is tmpList with calculated pay
    payLib = []
    # ot: overtime
    ot = 0
    # earnings: index 3  hours: index 2
    earnings = 0; hours = 0
    # do loop for each miniList in library
    for ct in lib:
        # if earnings is over 40:
        if int(ct[2]) > 40:
            # overtime is assigned total hours minus 40
            ot = int(ct[2]) - 40
            # overtime multiplied by time and a half
            ot = ot*1.5
            # hours set to 40
            hours = 40
        # if earnings is under 40:
        else:
            # hours assigned to hours
            hours = int(ct[2])
        # earnings assigned to hours*earnings + overtime*earnings
        earnings = (hours*int(ct[3]))+(ot*int(ct[3]))
        # create list(tmpLib); assign firstName,lastName,earnings to tmpLib
        tmpLib = [];tmpLib = [ct[0],ct[1],earnings]
        # append tmpLib to payLib
        payLib.append(tmpLib)
    # return payLib
    return payLib
    # post: none

# saveData() saves library neatly into file.txt
def saveData(file,lib):
    # pre: file must not exist, library must exist and be populated
    # tmpEmp is a string
    tmpEmp = ""
    # do loop for ct in library:
    for ct in lib:
        # do loop for index in ct:
        for index in ct:
            # add string of index plus a space to tmpEmp
            tmpEmp += str(index)+" "
        # add '\n' to tmpEmp for splitting later
        tmpEmp += '\n'
    # open file and assign to saveFile
    saveFile = open(file+".txt",'w')
    # write tmpEmp to the saveFile
    saveFile.write(tmpEmp)
    # return True for printing
    return True
    # post: none

# IMPORT
# os is used for checking if file exists
import os

# MAIN
# running creates a loop
running = True
# while running equals True
while running:
    # load data
    # print example
    print("Example: data")
    print("File must exist in directory")
    # assign user input to file
    file = input("Please enter file to be loaded: ")
    # while file already exists
    while os.path.exists(file+".txt") == False:
        # print file not found
        print("ERROR: file not found...")
        # print example
        print("Example: data")
        # asspign user input to file
        file = input("Please enter file to be loaded: ")
    # if file doesn't exists create library and assign the return of loadData(file) to library
    library = [];library = (loadData(file))

    # calc grosspay
    # print calculating gross pay
    print("Calculating Gross Pay...")
    # create list payRollLib; assign the return of calcPay(library) to payRollLib
    payRollLib = [];payRollLib = (calcPay(library))
    
    # save data
    # print saving data
    print("Saving Data...")
    # print example
    print("Example: myOutFile")
    # assign file to user input
    file = input("Please enter save file name: ")
    # while file exists:
    while os.path.exists(file) == True:
        # print error
        print("ERROR: file exsists already...")
        # print example
        print("Example: myOutFile")
        # assign file to user input
        file = input("Please enter save file name: ")
    # if the return of saveData(file,payRollLib) equals True:
    if saveData(file,payRollLib) == True:
        # print file saved as: string(file)
        print("File saved as: "+str(file))
    # close loop by assigning running to False
    running = False
# print done
print("Done")
