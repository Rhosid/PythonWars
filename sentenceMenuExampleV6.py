"""
Name: sentenceMenuExample.py
Description: This program rips apart the user's sentence
             and spits out cool info as requested.
Version: 1.0.6
Python: 3.3.5
"""

__author__ = "Spencer Dockham"
__date__ = "10/31/2014"

# use Count meth.

# def
def printMenu():
    # print menu with the following options and makes
    # sure their choice is numeric and within range.
    print("--------------------------")
    print("1. Number of Vowels"); print("2. Number of Consonants")
    print("3. Number of Spaces"); print("4. Number of Punctuation")
    print("5. List Words"); print("6. All of the Above"); print("7. Quit")
    tmp = input("Please select an option:")
    llist = ['1','2','3','4','5','6','7']
    while tmp not in llist:
        print("Choice must be between 1-6.")
        print("1. Number of Vowels"); print("2. Number of Consonants")
        print("3. Number of Spaces"); print("4. Number of Punctuation")
        print("5. List Words"); print("6. All of the Above"); print("7. Quit")
        tmp = input("Please select an option:")
    return tmp

def countVowel(tmp):
    # number of vowels.
    # check if every letter
    # is in the vowel list.
    # return as integer.
    tmp = tmp.lower()
    ct = 0
    for let in tmp:
        if let in vowelList:
            ct += 1
    return ct

def countCon(tmp):
    # number of consonants.
    # check if every letter
    # is in the con list.
    # return as integer.
    tmp = tmp.lower()
    ct = 0
    for let in tmp:
        if let in conList:
            ct += 1
    return ct

def countSpace(tmp):
    # number of spaces.
    # check every character
    # for being a space.
    # return as integer.
    ct = 0
    for let in tmp:
        if let in " ":
            ct += 1
    return ct

def countPun(tmp):
    # number of punctuation marks.
    # only searching for: ?.,! in punList.
    # return as integer.
    ct = 0
    for let in tmp:
        if let in punList:
            ct += 1
    return ct
    
def getWord(tmp):
    # list of words.
    # do not count punctuation: ?.,!
    # replace commas and double spaces
    # with only a single space.
    # returns a list of words.
    tmp = tmp.lower()
    words = ""
    for let in tmp:
        if let in megabet:
            words += str(let)
    words = words.replace(","," ")
    words = words.replace("  "," ")
    return words

def getSentence():
    # obtain a sentence from the user.
    # return sentence.
    tmp = input("Please enter a sentence: ")
    return tmp

# LISTS
#megabet used for getWord(tmp) function.
megabet = ['a','b','c','d','e','f','g','h','i','j',
           'k','l','m','n','o','p','q','r','s','t',
           'u','v','w','x','y','z',', ',' ',',']
# vowelList used for countVowel(tmp) function.
vowelList = ['a','e','i','o','u']
# conList used for countCon(tmp) function.
conList = ['b','c','d','f','g','h','j','k','l','m',
       'n','p','q','r','s','t','v','w','x','y','z']
# punList used for countPun(tmp) function.
punList = ['?','.',',','!']

# MAIN
running = True
# call getSentence to obtain sentence to work with.
sentence = getSentence()
while running:
    # call printMenu to obtain user's choice.
    choice = printMenu()
    # call appropriate functions, depending on the user's choice.
    if choice == '1':
        # count number of vowels.
        print("_"*26);print("Sentence: "+sentence)
        vowel = countVowel(sentence)     
        print("Vowels: " + str(vowel))
    elif choice == '2':
        # count number of consonants.
        print("_"*26);print("Sentence: "+sentence)
        con = countCon(sentence)         
        print("Consonants: " + str(con))
    elif choice == '3':
        # count spaces in sentence.
        print("_"*26);print("Sentence: "+sentence)
        space = countSpace(sentence)     
        print("Spaces: " + str(space))
    elif choice == '4':
        # count puncuation in sentence.
        print("_"*26);print("Sentence: "+sentence)
        pun = countPun(sentence)         
        print("Puncuations: " + str(pun))
    elif choice == '5':
        # count number of words.
        print("_"*26);print("Sentence: "+sentence)
        word = getWord(sentence)         
        print("Words: " + str(word))
    elif choice == '6':
        print("_"*26);print("Sentence: "+sentence)
        vowel = countVowel(sentence)     # count number of vowels.
        con = countCon(sentence)         # count number of consonants.
        space = countSpace(sentence)     # count spaces in sentence.
        pun = countPun(sentence)         # count puncuation in sentence.
        word = getWord(sentence)         # count number of words.
        print("--------------------------")
        print("Vowels: " + str(vowel)); print("Consonants: " + str(con))
        print("Spaces: " + str(space)); print("Puncuations: " + str(pun))
        print("Words: " + str(word))
    elif choice == '7':
        # exit loop by setting running to false.
        running = False
    else:
        # this statement will never be called. It is just an extra saftey net.
        print("Error reading choice, please choose again...")
    # ask user if they'd like to continue.
    tmp = input("Continue? [Enter] || Exit? [Type Any]")
    if tmp != "":
        running = False
# end program.
print("done")
    






