#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 11:21:03 2022

@author: chiehyulai
"""

x = int(input("Enter an interger: "))
# =============================================================================
# ans = 0
# while ans**3 < x:
# #    ans = ans + 1
#     ans += 1
# if ans**3 != x:
#     print(str(x) + " is not a perfect tube")
# else:
#     print("Cube root of " + str(x) + " is " + str(ans))
# 
# =============================================================================

# =============================================================================
# cube = x
# for guess in range(cube+1):
#     if guess**3 == cube:
#         print("Cube root of", cube, "is", guess)
# 
# =============================================================================


cube = x
for guess in range(abs(cube)+1):
    if guess**3 >= abs(cube):
        break
if guess**3 != abs(cube):
    print(cube, "is not a perfect cube")
else:
    if cube < 0:
        guess = -guess
    print("Cube root of " + str(cube) + " is " + str(guess))

