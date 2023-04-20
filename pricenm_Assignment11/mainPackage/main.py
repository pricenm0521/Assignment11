# main.py

# Name: Nicole Price
# email: pricenm@mail.uc.edu
# Assignment Title: Assignment 11
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: This is an in-class assignment
# Citations: In-Class work on 4/6/2023, assorted stackoverflow questions
# Anything else that's relevant: Modified donor code from Prof. Nicholson

# entry point only, no modifications to code here

from functionsPackage.functions import *

# problem 1
f = [-100, 0, 32, 100, 212]
Fahrenheit = np.array(f)
print(problem1(Fahrenheit))

# problem 2
a1 = np.array([1,2,3,4,5,6,7,8,9,10])
a2 = np.array([2,4,6,8,10,12,14,16,18,20])
print(problem2(a1,a2))

# problem 3
p3 = np.array([3,6,9,10,11,12,13,14,15,16,17,18])
print(problem3(p3))

# problem 4
print(problem4(1))

# problem 5
a = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13])
print(problem5(a))

# problem 6
names = np.array(['calbert cheaney', 'lyndon jones', 'pat graham', 'chris reynolds', 'matt nover', 'greg graham', 'todd leary'], dtype=str)
# on line 38 had to update dtype==np.str to str due to an error that np.str was depracated
print(problem6(names))
