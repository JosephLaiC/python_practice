#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 23:09:56 2022

@author: chiehyulai
"""

x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 - x) >= epsilon:
        guess += step
        
if abs(guess**2 - x) >= epsilon:
    print("failed")
else:
    print("succeeded: " + str(guess))


# =============================================================================
# 
# x = 16
# epsilon = 0.01
# step = 0.1
# guess = 0.0
# 
# while abs(guess**2 - x) >= epsilon:
#     if guess <= x:
#         guess += step
#     else:
#         break
#         
# if abs(guess**2 - x) >= epsilon:
#     print("failed")
# else:
#     print("succeeded: " + str(guess))
# =============================================================================
