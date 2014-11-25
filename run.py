"""
Name: run.py
Description: menu holding all programs in Programs folder
Version: 1.0.1
Python: 3.3.5
"""

__author__ = "Spencer Dockham"
__date__ = "11/25/2014"

# def
def editPath():
    tmpList = []
    print("EXAMPLES: C D G")
    localDisk = input("Please enter Local Disk Letter: ")
    #C:\\
    tmpList.append(localDisk.title())
    #C:\\Users\\
    tmpList.append("Users")
    print("EXAMPLE: Joe")
    compName = input("Please enter Comp Users's Name: ")
    #C:\\Users\\Spencer\\
    tmpList.append(compName.title())
    #C:\\Users\\Spencer\\Documents
    tmpList.append("Documents")
    #C:\\Users\\Spencer\\Documents\\GitHub\\
    tmpList.append("GitHub")
    print("EXAMPLE: pythonWars")
    repository = input("Please enter Repository name: ")
    #C:\\Users\\Spencer\\Documents\\GitHub\\Repository\\
    tmpList.append(repository.title())
    #C:\\Users\\Spencer\\Documents\\GitHub\\Repository\\Projects\\
    tmpList.append("Projects")
    
    # create path from list
    path = str(tmpList[0])+":"
    for ct in range(0,len(tmpList)-1):
        path += "\\"+str(tmpList[ct+1])

    return path

# credit: tzot
def fileCount(inDir):
    joiner= (inDir + os.path.sep).__add__
    return sum(
        os.path.isfile(filename)
        for filename
        in map(joiner, os.listdir(inDir))
    )

# import
import os
import time

# MAIN


#         Disk[0] User[1] Name[2]   Docs[3]    Git[4]  Repository[5] SubFolder[6]
#pathData = ['C','Users','Spencer','Documents','GitHub','PythonWars','Projects']

# request path from user
path = editPath()

# inform user that programs are being looked for
print("Searching for programs...")

print("path: "+str(path))

# if file found, continue
while os.access(path, os.F_OK) == False:
    print("Files not found...")
    path = editPath()
# if file not found, create or find file
else:
    print("Path found...")

# display menu
length = fileCount(path)
#for ct in range(0,length):
    #print(str(ct+1)+": "+

print("opening program...")
os.chdir(path)
os.system("start acronymGenerator.py")

print("Done")
# pause keeps the command window open
pause = input("Press any key to end: ")

