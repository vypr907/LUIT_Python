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

#variables
numInstances = 0 #stores the number of names the user needs
deptName = "" #stores the user's department name
instanceName = "" #container
loopy = 0

#get input
deptName = input("What department do you work in? ")
numInstances = int(input("How many instances are you creating? "))

#do the thing
while loopy < numInstances:
    print("beep")
    loopy += 1
