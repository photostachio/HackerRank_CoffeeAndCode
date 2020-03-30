# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 09:19:26 2020

@author: User
"""

def is_leap(year):
    leap = False
    
    if year % 400 == 0:
        return('True')
    if year % 100 == 0:
        return(leap)
    if year % 4 == 0:
        return('True')
    
    return leap

year = int(input())
print(is_leap(year))