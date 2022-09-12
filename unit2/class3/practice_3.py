#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 23:34:23 2022

@author: chiehyulai
"""

# =============================================================================
# x = 100000
# epsilon = 0.01
# numGuesses = 0
# low = 1.0
# high = x
# ans = (high + low)/2.0
# 
# while abs(ans**2 - x) >= epsilon:
#     print("low = " + str(low) + " high = " + str(high) + " ans = " + str(ans))
#     numGuesses += 1
#     if ans**2 < x:
#         low = ans
#     else:
#         high = ans
#     ans = (high + low)/2.0
# print("numGuesses = " + str(numGuesses))
# print(str(ans) + " is close to square root of " + str(x))
#         
# =============================================================================


high_str="Enter 'h' to indicate the guess is too high."
low_str="Enter 'l' to indicate the guess is too low."
correct_str="Enter 'c' to indicate I guessed correlty."

low = 0
high = 100
ans = int((low + high)/2)

print("Is your secret number is " + str(ans) + "?")
x = input(high_str + " " + low_str + " " + correct_str + " ")

if x == "l":
    low = ans
elif x == "h":
    high = ans 
elif x == "c":
    print("Game over. Your secret number was:", ans)
else:
    print("Sorry, I did not understand your input.")



ans=91

low = 0
high = 100
x = int((low + high)/2)
while int(x) != ans:
    if int(x) < ans:
        print("number", x, "is lower")
        low = x
    else:
        print("number", x, "is higher")
        high = x
    x = int((low + high)/2)
print("answer is correct")
print("Game over. Your secret number is:", x)
    





