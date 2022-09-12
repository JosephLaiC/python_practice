#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 21:20:10 2022

@author: chiehyulai
"""

### string[start:stop:step]

# =============================================================================
# s="abcdefgh"
# 
# s[::-1]
# s[3:6]
# s[-1]
# 
# =============================================================================

## 
s = "abcdefghi"

for index in range(len(s)):
    if s[index] == "i" or s[index] == "u":
        print("There is an i or u")

for char in s:
    if char == "i" or char == "u":
        print("There is an i or u")



an_letters = "aefhilmnorsxAEFHILMNORSX"

word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiam level (1-10): "))
i = 0

while i < len(word):
    char = word[i]
    if char in an_letters:
        print("Give me an " + char + "! " + char)
    else:
        print("Give me a " + char + "! " + char)
    i += 1
print("What does that spell?")
for i in range(times):
    print(word, "!!!")

