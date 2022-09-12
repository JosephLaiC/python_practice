# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 20:18:24 2022

@author: joseph
"""

def f(x):
    x = x + 1
    print('in f(x): x =', x)
    return x
x = 3
z = f(x)



def f(y):
    x = 1
    x += 1
    print(x)
    
x = 20
f(x)
print(x)
