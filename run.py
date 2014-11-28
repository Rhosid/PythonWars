"""
Name: run.py
Description: menu holding all programs in Programs folder
Version: 1.0.3
Python: 3.3.5
"""

__author__ = "Spencer Dockham"
__date__ = "11/27/2014"

# def
def checkPath(path):
    while os.access(path, os.F_OK) == False:
        return False
    else:
        return True

# credit: tzot
def fileCount(inDir):
    joiner= (inDir + os.path.sep).__add__
    for fileName in map(joiner,os.listdir(inDir)):
        return sum(
        os.path.isfile(filename)
        for filename
        in map(joiner, os.listdir(inDir))
    )

def regFiles(path,fileCt):
    lib = [] # lib will be returned to library
    foo = (path + os.path.sep).__add__
    # each loop filePath equals full path of program
    for filePath in map(foo,os.listdir(path)):
        tpl = ()
        # each loop a tpl is appended to lib
        #for ct in range(0,fileCt):
        fullPath = filePath.split('\\')
        pthLn = int(len(fullPath)-1); file = fullPath[pthLn]
        tpl = (file,filePath)
        lib.append(tpl)
    return lib

def printMenu(lib):
    numbet = []
    for ct in range(0,len(lib)):
        numbet.append(int(ct+1))
        data = lib[ct]
        print(str(ct+1)+". "+data[0])
    choice = input("Please enter a choice: ")
    while int(choice) not in numbet:
        print("Choice not valid. Please enter a number.")
        choice = input("Please enter a choice: ")
    else:
        foo = library[int(choice)-1]
        address = foo[1]
        return address

# import
import os

# MAIN

# standard path for pythonWars run program
path = os.path.dirname(os.path.realpath(__file__))
path += "\\Projects"

# inform user that programs are being looked for
print("Searching for programs...")

print("current path: "+str(path))

# if file found, continue
if checkPath(path):
    print("Path found...")
    running = True
    while running:
        
        # display menu
        #--------------------------------------------------
        # fileCt equals number of files in \Projects\*.py
        fileCt = fileCount(path)
        # library holds tuples of file name and path
        library = regFiles(path,fileCt)
        # assign path returned from printMenu to int(address)
        address = printMenu(library)
        print("opening program...")
        os.system("start "+str(address))
        #--------------------------------------------------

        tmpList = ['y','n']
        tmp = input("Contiue? [y/n]: ")
        while tmp.lower() not in tmpList:
            print("ERROR: Couldn't read choice...")
            tmp = input("Contiue? [y/n]: ")
        else:
            if tmp.lower() == 'y':
                print("")
            else:
                running = False
                break

# if file is not found, end program    
else:
    print("Files not found...")
    
# program concluded
print("Done")
