# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:50:38 2019

@author: Clint Mooney
"""

class Clock():
    # Override Built-In Class Functions:
    def __init__(self, hour=0, minutes=0, seconds=0):
        self.hour = self.checkInput(hour, 0)
        self.minutes = self.checkInput(minutes, 0)
        self.seconds = self.checkInput(seconds, 0)
    
    def __str__(self):
        return "The time is {}:{}:{}".format(self.hour, self.minutes, self.seconds)
    
    def __repr__(self):
        return self.__str__()
    
    # Override arithmetic operators:
    def __add__(self, to_be_added):
        if type(to_be_added) == Clock:
            new_hour = self.hour + to_be_added.hour
            new_mins = self.minutes + to_be_added.minutes
            new_secs = self.seconds + to_be_added.seconds
            return Clock(new_hour, new_mins, new_secs)
        else:
            new_hour = self.checkInput(to_be_added, 0)
            return Clock(new_hour, self.minutes, self.seconds)
    
    #   Make addition communicative:
    def __radd__(self, to_be_added):
        return self.__add__(to_be_added)
    
    # Function to streamline input management (Ensures input results in an int):
    def checkInput(self, input_time, default):
        if type(input_time) == int:
            return input_time
        elif type(input_time) == str:
            if input_time.isdigit():
                return int(input_time)
            else:
                print("Argument provided not a number. Setting affected input to '{}.'".format(default))
                return default
        elif type(input_time) == float:
            return int(input_time)
        else:
            print("Argument provided not a number. Setting affected input to '{}.'".format(default))
            return default

new_clock = Clock(5, 14, 30)
print(new_clock)
print(str(new_clock))
print(new_clock + Clock(1, 1, 10))
print(new_clock + 1)
print(new_clock + 1.0)
print(new_clock + "1")
print(new_clock + "Bop")
print(1 + new_clock)
print(1.0 + new_clock)
print("1" + new_clock)
print("Bop" + new_clock)