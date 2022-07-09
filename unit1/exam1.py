#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 12:12:42 2022

@author: chiehyulai
"""

s = "azcbobobegghakl"

# =============================================================================
# for i in range(len(s)):
#     check = s[i]
#     if check == "a" or check == "e" or check == "i"\
#         or check == "o" or check == "u":
#             print("Number of vowels: ", i)
# =============================================================================


            
# =============================================================================
# letter = "bob"
# hit = 0
# for i in range(len(s)-len(letter)):
#     word = s[i] + s[i+1] + s[i+2]
#     if word == letter:
#         hit += 1
# print("Number of times bob is:", hit)
# =============================================================================



s = "abcdcb" 
alphabet = "abcdefghijklmnopqrstuvwxyz"
ans = ""

for i in range(len(alphabet)):
    for j in range(i, len(alphabet)):
        check = alphabet[i:j+1]
        if check in s:
            if len(check) > len(ans):
                ans = check
print("Longest substring in alphabetical order is:", ans)



