#!/usr/bin/ python3.7

import math
import os
import random
import re
import sys

base_2 = []

if __name__ == '__main__':
    n = int(input("Enter a number to convert to binary: ").strip())

#convert to binary______________________________
while n > 0:
    remainder = int(n%2)
    n = int(n/2)
    base_2 = [remainder] + base_2
#_______________________________________________

#now find the number of consecutive 1's_________
high_score = 0
count = 0
for digit in base_2:
    if digit == 1:  #found a 1, add it to the counter
        count += 1
    else: #not a 1, add the current count to the high score and reset
        if count > high_score:
            high_score = count
        count = 0
#_______________________________________________

print(''.join(str(num) for num in base_2))
print("Consecutive '1's:",high_score)