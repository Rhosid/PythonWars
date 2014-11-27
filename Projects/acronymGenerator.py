"""
Name: acronymGenerator.py
Stuffs: by Spencer and Nick!
Date: 10/29/14
"""

# DEF

def acroGen(string):
    string = string.title()
    acro = ""
    for ch in string:
        if ch in capabet:
            acro += ch
    return acro

# LISTS

capabet = ['A','B','C','D','E','F','G','H','I','J',
           'K','L','M','N','O','P','Q','R','S','T',
           'U','V','W','X','Y','Z']

# MAIN

# acronym generator
print("acronymGenerator.py")
string = input("Please Enter String: ")
acro = acroGen(string)
print("Acronym: "+acro)
