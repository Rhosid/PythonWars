"""
Name: hangman.py
Description: game of hangman
Version: 1.0.2
"""

__author__ = "Spencer Dockham"
__date__ = "12/4/2014"

# IMPORT
import random

# DEF
def getSecret():
    # pre: none
    words = ['fish','banana','poster','hampster','house','python','bonus','water','yellow','star']
    random.shuffle(words)
    return words[0]

def testLetter(let,secret):
    # pre: let must be in alphabet, secret must be populated
    for ch in secret:
        if let == ch:
            return True
    return False

def printWord(List,secret):
    # pre: secret must be populated
    encode = ''
    for ch in secret:
        if ch in List:
            encode+=ch
        else:
            encode+='*'
    return encode

def checkWin(word):
    # pre: word must be populated
    for ch in word:
        if ch == '*':
            return False
    return True

def inList(word,List):
    # pre: word and List must be populated
    if word in List:
        return True
    else:
        return False

def displayWrong(falseList):
    # pre: falseList must exist
    tmp = ''
    for ct in range(0,len(falseList)):
        tmp+=falseList[ct]+' '
    print("Wrong Guesses: "+str(tmp))

def debugRequest():
    # pre: none
    tmpList = ['y','n']
    tmp = input("DEBUG MODE? [y/n]: ")
    while tmp.lower() not in tmpList:
        print("ERROR: Couldn't read choice...")
        tmp = input("DEBUG MODE? [y/n]: ")
    else:
        if tmp.lower() == 'y':
            print('debug mode turned on...')
            return True
    return False
    
# LIST
alphabet=['a','b','c','d','e','f','g','h','i','j',
          'k','l','m','n','o','p','q','r','s','t',
          'u','v','w','q','y','z']

# MAIN
print("HangMan")
DEBUG_MODE = debugRequest()
falseList = [] # list with false letters in
trueList = [] # list with true letters in
guessList = []
turns = 10 # number of turns to guess word
win = False; running = True
secret = getSecret() # assign secret the secret word

# while player wants to play
while running == True:
    falseList = [] # list with false letters in
    trueList = [] # list with true letters in
    guessList = []
    turns = 10 # number of turns to guess word
    win = False; running = True
    secret = getSecret() # assign secret the secret word
    # while they haven't won
    while win == False:
        # while they haven't lost
        while turns > 0:
            print('\n'*50)
            print("HangMan\n")
            print("=+="*15)
            print("Round: "+str(turns))
            displayWrong(falseList)
            print("-"*45);print('')
            print("Word: "+str(printWord(trueList,secret)))
            if DEBUG_MODE: # if debug is on display secret word
                print("DEBUG: Word: "+str(secret))
            print('');print("-"*45);print('')
            guess = input("Please guess a letter: ")
            guess = guess.lower()
            # while guess isn't in alphabet
            while guess not in alphabet:
                print("ERROR: Please enter only one letter...")
                guess = input("Please guess a letter: ")
                guess = guess.lower()
            guessList.append(guess)
            # if testLetter is true
            if testLetter(guess,secret) == True:
                print("Correct.")
                if inList(guess,trueList) == False:
                    trueList.append(guess)
                print('')
                print("Word: "+str(printWord(trueList,secret)));print('')
            # if testLetter is not true
            else:
                print("Incorrect.")
                if inList(guess,falseList) == False:
                    falseList.append(guess)
                    # subtract only if they guess wrong
                    turns-=1
            # check if word has any * in it
            if checkWin(printWord(trueList,secret)) == True:
                print('WINNER!!!\n')
                win = True
                break
            else:
                print('')
        else:
            print("You Lost...\n")
            break

    # once game is over request Play Again
    tmpList = ['y','n']
    tmp = input("Play Again? [y/n]: ")
    while tmp.lower() not in tmpList:
        print("ERROR: Couldn't read choice...")
        tmp = input("Play Again? [y/n]: ")
    else:
        if tmp.lower() == 'y':
            print('loading...')
        else:
            running = False
            break
print('Done.')


        
