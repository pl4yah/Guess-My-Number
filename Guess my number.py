#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 11:00:24 2019

@author: pl4yah
"""
print("Welcome to Guess My Number")
import random
number = random.randrange(1,100)

guess = int(input("\nInput your number guess between 1-100: "))

count = 1


while guess != number:
    count += 1
    if guess > number:
        print("\nGo lower")
        guess = int(input("Try again: "))
        continue
    else:
        print("\nGo higher")
        guess = int(input("Try again: "))
        continue
    

print("That's the number, you took", count,"tries.")