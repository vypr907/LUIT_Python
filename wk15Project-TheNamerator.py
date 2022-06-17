#!/user/bin/env python3.7

# --------------------------------------------------------------
# Program: The Namerator
# Programmer: Steven Laszloffy
# Project: LUIT Week 15
# Purpose: A simple program that generates EC2 names based on departments.
# - allow the user to input how many names they need
# - allow the user to input their department name to be used in the EC2 name
# - generate random characters and numbers that will be included in the name
# ---------------------------------------------------------------

import random
import string
import sys

#variables
numInstances = 0 #stores the number of names the user needs
deptName = "" #stores the user's department name
loopy = 0
instName = "" #container for instance name
authDepts = ['marketing','accounting', 'finops']
isMatch = True

abc = string.ascii_letters 

#get input
print("Welcome to The Namerator!")
print("-----------------------------------")
print("A Tool for the following Departments: ")
print("Marketing | Accounting | FinOps")
print("-----------------------------------")

deptName = input("What department do you work in? ")

for dept in authDepts:
    if deptName.lower() == dept:
        print("Department Authorized.")
        isMatch = True
        break #name matches authorized department
    else:
        isMatch = False
        
if isMatch == False:
    print("Sorry, this tool is not authorized for your department.")
    print("Goodbye.")
    sys.exit()
    
while True:
    try:
        numInstances = int(input("How many instances are you creating? "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue

    if numInstances < 0:
        print("Sorry, I can't create negative names.")
        continue
    else:
        #value was successfully parsed, and we're happy with its value.
        #we're ready to exit the loop.
        break

#do the thing
print()
print("--------------------------------")
print("Instance Names")
print("--------------------------------")
print()
while loopy < numInstances:
    #print("beep")
    loopy += 1
    instName = deptName.title()+"-"+str(loopy)+random.choice(abc)+str(random.randint(0,10))+random.choice(abc)
    print(instName)
