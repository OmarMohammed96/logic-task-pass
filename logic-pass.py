# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 11:10:49 2022

@author: Eng.omar
"""
#%%

# Q1

"""Remove any character from a string that is given by the user."""

print('This program helps you to remove any character from a given string.')

def input1():
    global string                                  # string need to be defined for other functions.
    string = input('Enter the string: ')          
    if string.isspace() or string.isdigit():       # condition to ensure that the input data is only string.
        print('Please enter a string!') 
        return input1()                            # repeat the input process.
    else: 
        input2()                                   

def input2():
    k = 0
    _lst = []
    global remove                                 # remove need to be defined for other functions. 
    remove = input('Enter the character: ')
    for z in remove:                              # loop to count the number of intered character in (remove).
        _lst.append(z)
        k +=1                                     # k represent the counter.       
    if remove.isspace() or remove.isdigit():      # condition to ensure that the input data is only characters.
        print('Please enter a character!')
        return input2()                           
    if k > 1:                                     # condition to check the number of entered characters.
        print('Please enter one character!')
        return input2()
    else:
        code()

def code():
    for x in string:                                # For loop to remove the selected character 
        if x == remove:
            continue 
        print(x, end='')                           # Print the character side by side to return the intered string without the removed character.

input1()

#%%

# Q2

"""Finding a prime number in a given range."""
# Prime number is natural number greater than 1, that has no positive divisors other than 1 and itself.

print('This program helps you find the prime number in any selected range.')

# the user need to inter the range.
lower = int(input('Enter the lower interval: '))
upper = int(input('inter the upper interval: '))

for number in range(lower,upper+1):
    if number > 1:                      # Prime number should be grater than 1.
        for x in range(2,number):       # The range start from 2 because prime number isgreater than 1.
            if number % x == 0:         # Check if the number in the range is divisibal by the all number smaller than it.
                break 
        else:
            print(number)

#%%

# Q3

"""Counting the number of given character in a given string."""

print('This program helps you to count the number of a specific character in any string.')

def input1():
    global string                                  # string need to be defined for other functions.
    string = input('Enter the string: ')          
    if string.isspace() or string.isdigit():       # condition to ensure that the input data is only string.
        print('Please enter a string!') 
        return input1()                            # repeat the input process.
    else: 
        input2()                                   

def input2():
    k = 0
    _lst = []
    global chara_                                  # chara_ need to be defined for other functions. 
    chara_ = input('Enter the character: ')
    for z in chara_:                               # loop to count the number of intered characters in (chara).
        _lst.append(z)
        k +=1                                      # k represent the counter.       
    if chara_.isspace() or chara_.isdigit():       # condition to ensure that the input data is only characters.
        print('Please enter a character!')
        return input2()                           
    if k > 1:                                      # condition to check the number of entered characters.
        print('Please enter one character!')
        return input2()
    else:
        code()

def code():
    z = 0                                          # z is used as a counter.
    for i in string:                               # This loop count the number of repeted character in the lst. we can directly count it from the string.
        if i == chara_:
            z += 1                          
        else:
            continue                               # Each time the previous condition is not achieved the program will back to start new loop.
  
    print('The number of character', '(', chara_, ')', 'in the string is: ', z)     # Print the result.
        
input1()
      












