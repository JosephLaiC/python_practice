#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 01:37:31 2022

@author: chiehyulai
"""

high_str="Enter 'h' to indicate the guess is too high."
low_str="Enter 'l' to indicate the guess is too low."
correct_str="Enter 'c' to indicate I guessed correlty."

low = 0
high = 100
ans = int((low + high)/2)

print("Please think of a number between 0 and 100!")

while ans > 0 & ans < 100:
    print("Is your secret number is " + str(ans) + "?")
    x = input(high_str + " " + low_str + " " + correct_str + " ")
    
    if x == "l":
        low = ans
    elif x == "h":
        high = ans 
    elif x == "c":
        print("Game over. Your secret number was:", ans)
        break
    else:
        print("Sorry, I did not understand your input.")
    ans = int((low + high)/2)


## Ans
# =============================================================================
# print("Please think of a number between 0 and 100!")
# 
# # At the start the highest the number could be is 100 and the lowest is 0.
# hi = 100
# lo = 0
# guessed = False
# 
# # Loop until we guess it correctly
# while not guessed:
#     # Bisection search: guess the midpoint between our current high and low guesses
#     guess = (hi + lo)//2
#     print("Is your secret number " + str(guess)+ "?")
#     user_inp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
# 
#     if user_inp == 'c':
#         # We got it right!
#         guessed = True
#     elif user_inp == 'h':
#         # Guess was too high. So make the current guess the highest possible guess.
#         hi = guess
#     elif user_inp == 'l':
#         # Guess was too low. So make the current guess the lowest possible guess.
#         lo = guess
#     else:
#         print("Sorry, I did not understand your input.")
# 
# print('Game over. Your secret number was: ' + str(guess))
# =============================================================================
