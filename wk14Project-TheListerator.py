#!/usr/bin/env Python3.7

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
file = open('LUIT_Python/services.txt','r')
for line in file:
    strippedLine = line.strip()
    services.append(strippedLine)
    
#print the list
print(services)

#print the length
print("The list has",len(services),"entries.")

