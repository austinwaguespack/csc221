#!/usr/bin/env python3

import hw4_solution
# --------------------------------------------------------------------
# Problem 1
# 
# Create a function, is_odd, that takes a number and returns True if
# that number is odd.
# 
# Function: is_odd
# 
# parameters:
# - number
#
# returns: boolean
def is_odd(number):
    return number%2==1

# --------------------------------------------------------------------
# Problem 2
# 
# Create a function, is_even, that takes a number and returns True if
# that number is even. 
# 
# Function: is_even
# 
# parameters:
# - number
#
# returns: boolean
def is_even(number):
    return number%2==0


# --------------------------------------------------------------------
# Problem 3
# 
# Create a function, is_mult_of_four, that takes a number and returns
# True if that number is a multiple of four. 
# 
# Function: is_mult_of_four
# 
# parameters:
# - number
#
# returns: boolean
def is_mult_of_four(number):
    return number/4==0


# --------------------------------------------------------------------
# Problem 4
# 
# Create a function, is_mult_of_x, that takes a number and a divisor
# and returns True if that number is divisible by divisor
# 
# Function: is_mult_of_divisor
# 
# parameters:
# - number
# - divisor
#
# returns: boolean
def is_mult_of_divisor(number, divisor):
    return number/divisor==0


# --------------------------------------------------------------------
# Problem 5
# 
# Given a string s, return a string made of the first 2 and the last 2
# chars of the original string, so 'spring' yields 'spng'. However, if
# the string length is less than 2, return instead the empty string.
#
# Function: both_ends
#
# parameters:
# - s
#
# returns: string
def both_ends(s):
    if string >2:
        return ''
    else:
        return s[1, 2, -1, -2]
