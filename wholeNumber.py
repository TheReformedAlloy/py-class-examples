# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:52:27 2019

@author: Clint Mooney
"""

class wholeNumber():
    # Override Built-In Class Functions:
    def __init__(self, number):
        if number >= 0:
            self.number = number
    
    def __repr__(self):
        return str(self.number)
    
    # Check If Given Types Are wholeNumbers
    def is_whole(self, unknown):
        if type(unknown) is wholeNumber:
            return True
        else:
            return False
    
    # Override Arithmetic Operators:
    def __add__(self, num2):
        if self.is_whole(num2):
            num3 = self.number + num2.number
            return wholeNumber(num3)
        else:
            raise TypeError
    
    def __sub__(self, num2):
        if self.is_whole(num2):
            num3 = self.number - num2.number
            return wholeNumber(num3)
        else:
            raise TypeError
    
    def __mul__(self, num2):
        if self.is_whole(num2):
            num3 = self.number * num2.number
            return wholeNumber(num3)
        else:
            raise TypeError

try:
    new_num = wholeNumber(-100)
    print(new_num)
    new_num = new_num - wholeNumber(87)
    print(new_num)
    new_num = new_num * wholeNumber(13)
    print(new_num)
    new_num = new_num + wholeNumber(31)
    print(new_num)
    new_num = new_num + 1
except TypeError:
    print("Error: One of the above operations raised a TypeError event.")