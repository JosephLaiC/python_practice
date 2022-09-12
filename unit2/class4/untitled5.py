# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 20:02:14 2022

@author: joseph
"""

def foo(x, y = 5):
   def bar(x):
      return x + 1
   return bar(y * 2)

foo(3)


def foo(x, y = 5):
   def bar(x):
      return x + 1
   return bar(y * 2)

foo(3, 0)


def foo (x):
   def bar (z, x = 0):
      return z + x
   return bar(3, x)

foo(2)


def foo (x):
   def bar (z, x = 0):
      return z + x
   return bar(3)

foo(5)



def Benjamin_func(timeOfRead):
    if timeOfRead == 0:
        print("你會被當掉")
    elif timeOfRead > 0 and timeOfRead < 10:
        print("你可能還有救")
    else:
        print("很好")
