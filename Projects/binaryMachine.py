"""
Name: binaryMachine.py
Description: converts base10 to a different base#
Version: 1.0.0
"""

__author__ = "Spencer Dockham"
__date__ = "12/2/2014"

# DEF
def convertBase2(num):
    base = str("{0:b}".format(int(num)))
    return base

def convertBase8(num):
    base = str("{0:x}".format(int(num)))
    return base

def convertBase16(num):
    base = str("{0:o}".format(int(num)))
    return base

# MAIN

# Types
# Base 10: [0-9] [ex: 100]
# Base 2:  [0-1] [ex: 1100100] [pat: 1,2,4,8,16,32,64,128,256,512]
# Base 8:  [0-7] [ex: 64]      [pat: 1,8,64,512]
# Base 16: [0-F] [ex: 64]      [pat: 1,16,256,4096]

foo = True
while foo:
    base10 = input("Please enter a number: ")

    print("Base2: "+str(convertBase2(base10)))
    print("Base8: "+str(convertBase8(base10)))
    print("Base10: "+base10)
    print("Base16: "+str(convertBase16(base10)))
    tmpList = ['y','n']
    tmp = input("Contiue? [y/n]: ")
    while tmp.lower() not in tmpList:
        print("ERROR: Couldn't read choice...")
        tmp = input("Contiue? [y/n]: ")
    else:
        if tmp.lower() == 'y':
            print("")
        else:
            foo = False
            break

# program concluded
print("Done")
# pause keeps the command window open
pause = input("Press any key to end: ")
