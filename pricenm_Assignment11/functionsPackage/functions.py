# functions. py
from _elementtree import Element

# Name: Nicole Price
# email: pricenm@mail.uc.edu
# Assignment Title: Assignment 11
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: This is an in-class assignment
# Citations: In-Class work on 4/6/2023, assorted stackoverflow questions
# Anything else that's relevant: Modified donor code from Prof. Nicholson

'''
NumPy arrays and fun stuff
@author: nicomp
'''
import numpy as np
import random as random

# Problem #1: Here is a numPy array of Fahrenheit temperatures. Convert them to Centigrade temperatures and print the result
def problem1(arrayOfTemperatures):
    try:
        for i in range(0, len(arrayOfTemperatures)):
            # convert the element at index i to centigrade
            arrayOfTemperatures[i] = (arrayOfTemperatures[i] - 32)*(5/9)
        return arrayOfTemperatures
    except:
        return np.array([np.NaN])

# f = [-100, 0, 32, 100, 212] given code, moved to main
# Fahrenheit = np.array(f) given code, moved to main
#print(Fahrenheit)

# Problem #2: Given two arrays, find the common values between them. 
def problem2(np1, np2):
    problem2 = np.intersect1d(np1, np2)
    return problem2
#a1 = np.array([1,2,3,4,5,6,7,8,9,10]) given code, moved to main
#a2 = np.array([2,4,6,8,10,12,14,16,18,20]) given code, moved to main

# Problem #3: Given an array, a1, create a new array, a2, with all the values divisible by 3 in a1
def problem3(a1):
    a2 = []
    for x in a1:
        if x % 3 == 0:
            a2.append(x)
    return a2
#p3 = np.array([3,6,9,10,11,12,13,14,15,16,17,18]) given code, moved to main

# Problem #4: Create a 2-dimensional (2-axis) array with 5 rows and 6 columns. Initialize the elements to random integer values between 1 and 100
def problem4(randomArray):
    array = np.random.randint(1,100, size=(5,6))
    return array

# Problem #5: Given an array, a, compute the average of all the elements. Use a for loop and a flatten function.
def problem5(a):
    a_flat = a.flatten()
    sum = 0
    for y in a_flat:
        sum += y
    avg = [sum/len(a_flat)]
    return avg
# a = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13]) given code, moved to main

# Problem #6: Given an array of strings containing first/last names, convert them to title case.
def problem6(names):
    properNames = np.empty_like(names)
    for t, name in np.ndenumerate(names):
        properNames[t] = name.title()
    return properNames
# names = np.array(['calbert cheaney', 'lyndon jones', 'pat graham', 'chris reynolds', 'matt nover', 'greg graham', 'todd leary'], dtype=np.str) given code, moved to main


