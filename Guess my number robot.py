#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 11:00:24 2019

@author: pl4yah

Known issues:
    1. Only works if range is up to 100000000000000000 assuming 1 is low
    2. Probably quicker/more efficient algorithms, perhaps using binary
"""
print("Welcome to Guess My Number")
import random
import statistics

number = random.randrange(1,100)
guess = 50
upper_range = 100
lower_range = 1
count = 1

print(guess)

while guess != number:
    count += 1
    if guess < number:
        lower_range = guess
        guess = statistics.median([upper_range,lower_range])
        guess = int(guess)
        print(guess)
    else:
        upper_range = guess
        guess = statistics.median([lower_range,upper_range])
        guess = int(guess)
        print(guess)
    

print(number,"is the number, you took", count,"tries.")