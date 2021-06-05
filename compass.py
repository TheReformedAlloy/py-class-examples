# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:50:41 2019

@author: Clint Mooney
"""

class Compass():
    # Override Built-In Functions:
    def __init__(self, degrees=0, minutes=0):
        self.minutes = self.checkInput(minutes, 0)
        self.degrees = self.checkInput(degrees, 0)
        self.rolloverMinutes()
        self.rolloverDegrees()
    
    def __str__(self):
        return "We're facing {} degrees and {} minutes.".format(self.degrees, self.minutes)
    
    def __repr__(self):
        return self.__str__()
    
    # Overrides Arithmetic Operators:
    def __add__(self, to_be_added):
        if type(to_be_added) == Compass:
            new_degrees = self.degrees + to_be_added.degrees
            new_minutes = self.minutes + to_be_added.minutes
            return Compass(new_degrees, new_minutes)
        else:
            new_degrees = self.degrees + self.checkInput(to_be_added, 0)
            return Compass(new_degrees, self.minutes)
    
    #   Makes addition communicative:
    def __radd__(self, to_be_added):
        return self.__add__(to_be_added)
    
    # Function to ensure input is an int:
    def checkInput(self, input_orientation, default):
        if type(input_orientation) == int:
            return input_orientation
        elif type(input_orientation) == str:
            if input_orientation.isdigit():
                return int(input_orientation)
            else:
                print("Argument provided not a number. Setting affected input to '{}.'".format(default))
                return default
        elif type(input_orientation) == float:
            return int(input_orientation)
        else:
            print("Argument provided not a number. Setting affected input to '{}.'".format(default))
            return default
    
    # Function to ensure degrees always within 1 to 359:
    def rolloverDegrees(self):
        if self.degrees // 360 >= 1:
            self.degrees = self.degrees % 360
    
    # Function to ensure minutes always within 1 to 59:
    #   Adds multiples of 60 to degrees:
    def rolloverMinutes(self):
        if self.minutes // 60 >= 1:
            self.degrees += self.minutes // 60
            self.minutes = self.minutes % 60

new_compass = Compass(-360, 760)
print(new_compass)
print(str(new_compass))
print(new_compass + Compass(1, 1))
print(new_compass + 1)
print(new_compass + 1.0)
print(new_compass + "1")
print(new_compass + "Bop")
print(1 + new_compass)
print(1.0 + new_compass)
print("1" + new_compass)
print("Bop" + new_compass)