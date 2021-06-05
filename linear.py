# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:47:19 2019

@author: Clint Mooney
"""

class LinearEquation():
    # Override Built-In Class Function
    def __init__(self, m, b):
        self.slope = m
        self.y_intercept = b
    
    def __str__(self):
        return str(self.slope) + "x + " + str(self.y_intercept)
    
    def __repr__(self):
        string = str(self)
        return string
    
    #Override arithmetic operator:
    def __add__(self, equation2):
        new_slope = self.slope + equation2.slope
        new_intercept = self.y_intercept + equation2.y_intercept
        return LinearEquation(new_slope, new_intercept)
    
    # Return y value for given x value in equation:
    def value(self, x_value):
        y_value = (self.slope * x_value) + self.y_intercept
        return y_value
    
    # Return equation composed with another equation:
    #   Composition is essentially substituting variables for another equation:
    def compose(self, equation2):
        new_slope = self.slope * equation2.slope
        new_intercept = (self.y_intercept * equation2.slope) + equation2.y_intercept
        return LinearEquation(new_slope, new_intercept)

first_line = LinearEquation(2, 4)
second_line = LinearEquation(1,2)
print(str(first_line))
print("Bingo: " + str(second_line))
print(first_line.value(4))
print(second_line.value(4))
comp_line1 = first_line.compose(second_line)
print(str(comp_line1) + ":")
print(comp_line1.value(4))
comp_line2 = second_line.compose(first_line)
print(str(comp_line2) + ":")
print(comp_line2.value(4))
add_line = first_line + second_line
print(str(add_line))
print(add_line.value(4))