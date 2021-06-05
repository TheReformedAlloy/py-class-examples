# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:50:29 2019

@author: Clint Mooney
"""

class Odometer():
    # Override Built-In Class Functions:
    def __init__(self, distance=0, units="miles"):
        self.distance = float(distance)
        self.units = units
    
    def __str__(self):
        return str(round(self.distance, 1)) + " " + self.units
    
    def __repr__(self):
        return self.__str__()
    
    # Override Arithmetic Operators:
    def __add__(self, int_to_be_added):
        if type(int_to_be_added) == int or type(int_to_be_added) == float:
            new_distance = self.distance + int_to_be_added
            return Odometer(new_distance, self.units)
        else:
            print("You can only add numbers to the Odometer class.")
            return self
    
    #   Make addition communicative
    def __radd__(self, int_to_be_added):
        return self.__add__(int_to_be_added)
    
    def __sub__(self, int_to_be_subbed):
        new_distance = self.distance - int_to_be_subbed
        return Odometer(new_distance, self.units)
    
    # Unused functionality to convert miles to kms, or vice versa:
    def convertUnits(self, distance, to_miles):
        if to_miles:
            return distance / 1.61
        else:
            return distance * 1.61

new_odometer = Odometer(5, "miles")
print(new_odometer)
print(str(new_odometer))
print(new_odometer + Odometer(1, "kilometers"))
print(new_odometer + 1)
print(new_odometer + 1.0)
print(new_odometer + 1.16)
print(new_odometer + "1")
print(new_odometer + "Bop")
print(1 + new_odometer)
print(1.0 + new_odometer)
print(new_odometer + 32.5)
print("1" + new_odometer)
print("Bop" + new_odometer)