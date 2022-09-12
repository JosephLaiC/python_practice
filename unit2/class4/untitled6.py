# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 23:26:05 2022

@author: joseph
"""

def multi_iter(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result


def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

##-----------------------------##
def iterPower(base, exp):
    result = base
    if exp <= 0:
        return 1
    else:
        while exp > 1:
            result = result*base
            exp -= 1
        return result

## Real ans
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    result = 1
    while exp > 0:
        result *=base
        exp -= 1
    return result
##----------------------------##

def recurPower(base, exp):
    if exp <= 0:
        return 1
    return base * recurPower(base, exp - 1)




         