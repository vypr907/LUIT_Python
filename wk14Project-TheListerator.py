#!/usr/bin/env python3.7

# --------------------------------------------------------------
# Program: The Listerator
# Programmer: Steven Laszloffy
# Project: LUIT Week 14
# Purpose: A simple program that creates a list of AWS services.
# - initially empty
# - must populate using append or insert
# - print the list and length of the list
# - remove two specific services from the list by name or index
# - print the new list and the new length
# ---------------------------------------------------------------

# create the list
services = []

#populate the list from text file
file = open('services.txt','r')
for line in file:
    strippedLine = line.strip()
    services.append(strippedLine)
    
#print the list
print(services)

#print the length
print("The list has",len(services),"entries.")

#remove two services from the list by name or by index
#for giggles, letting the user pick via number.. and for time, 
# we are assuming they won't try and break the fragile code and my heart...
print("AWS is downsizing it's services, and you get to pick which two get the axe!")
print("Please enter a number between 1 and",len(services),":",end = ' ')
choiceOne = int(input())
choiceTwo = int(input("Please enter your second pick: "))
#adjusting to index
choiceOne = choiceOne - 1
choiceTwo = choiceTwo - 1
print("Great picks! Say goodbye to", services[choiceOne], "and", services[choiceTwo],":)")
#deleting the chosen values
del services[choiceOne]
del services[choiceTwo-1]

#print the new list and the new length
print("The new list is: ",services, "and the length is",len(services))
