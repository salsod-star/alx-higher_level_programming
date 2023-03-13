#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """Print out all elements in a list in reverse"""
    
    for el in my_list[::-1]:
        print('{:d}'.format(el))
