# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 21:10:20 2022

@author: joseph
"""

def multi_iter(a, b):
    result = 0 
    while b > 0:
        result += a
        b -= 1
    return result

def multi(a, b):
    if b == 1:
        return a
    else:
        return a + multi(a, b-1)



##--------------------------##


def printMove(fr, to):
    print("move from " + str(fr) + " to " + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(n, fr, to, spare)
        Towers(n-1, spare, to, fr)


def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a > b:
        result = b
        while b > 1:
            if a%result == 0 and b%result == 0:
                return result
            else:
                result -= 1
    else:
        result = a
        while a > 1:
            if a%result == 0 and b%result == 0:
                return result
            else:
                result -= 1
                
                
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Base case is when b = 0
    if b == 0:
        return a

    # Recursive case
    return gcdRecur(b, a % b)
