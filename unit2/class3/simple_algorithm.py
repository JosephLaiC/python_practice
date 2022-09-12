#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 12:39:05 2022

@author: chiehyulai
"""

## Newton-Raphson
epsilon = 0.01
y = 24.0
guess = y/2.0
numGuesses = 0

while abs(guess*guess - y) >= epsilon:
    numGuesses += 1
    guess = guess - ((guess**2 - y)/(2*guess))
print("numGuess = " + str(numGuesses))
print("Square root of " + str(y) + " is about " + str(guess))
 


## bisection
x = 24
epsilon = 0.01
numGuesses = 0
low = 1.0
high = x
ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon:
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print("numGuesses = " + str(numGuesses))
print(str(ans) + " is close to square root of " + str(x))
        

