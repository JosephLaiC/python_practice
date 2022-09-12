# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 20:59:34 2022

@author: joseph
"""

def a(x, y, z):
     if x:
         return y
     else:
         return z

def b(q, r):
    return a(q>r, q, r)


x = 12
def g(x):
      x = x + 1
      def h(y):
          return x + y
      return h(6)
g(x)


def printName(firstName, lastName, reverse):
    if reverse:
        print(lastName + ", " + firstName)
    else:
        print(firstName + ", " + lastName)