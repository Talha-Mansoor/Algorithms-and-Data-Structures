# CMPT 145 Course material
# Copyright (c) 2017-2020 Michael C Horsch
# All rights reserved.
#
# This document contains resources for homework assigned to students of
# CMPT 145 and shall not be distributed without permission.  Posting this 
# file to a public or private website, or providing this file to a person 
# not registered in CMPT 145, constitutes Academic Misconduct, according 
# to the University of Saskatchewan Policy on Academic Misconduct.
# 
# Synopsis:
#   Implements the Stack ADT
#
# A stack (also called a pushdown or LIFO stack) is a compound 
# data structure in which the data values are ordered according 
# to the LIFO (last-in first-out) protocol.
#
# Implementation:
# This implementation uses the linked node structure.


import Node as N

class Stack(object):

    def __init__(self):
        """
        Purpose
            creates an empty stack
        """
        self.__size = 0      # how many elements in the stack
        self.__top = None    # the node chain starts here



    def size(self):
        """
        Purpose
            returns the number of data values in the stack
        Return:
            The number of data values in the stack
        """
        return self.__size


    def is_empty(self):
        """
        Purpose
            checks if the stack has no data in it
        Return:
            True if the stack has no data, or false otherwise
        """
        return self.__size == 0


    def push(self, value):
        """
        Purpose
            adds the given data value to the stack
        Pre-conditions:
            value: data to be added
        Post-condition:
            the value is added to the stack
        Return:
            (none)
        """
        new_node = N.node(value, self.__top)
        self.__top = new_node
        self.__size += 1


    def pop(self):
        """
        Purpose
            Removes and returns a data value from the stack.
            Note: the stack cannot be empty!
        Post-condition:
            the first value is removed from the stack
        Return:
            the first value in the stack, or None
        """
        assert not self.is_empty(), 'popped an empty stack'

        prev_first_node = self.__top
        result = prev_first_node.get_data()
        self.__top = prev_first_node.get_next()
        self.__size -= 1
        return result


    def peek(self):
        """
        Purpose
            returns the value from the top of given stack
            without removing it
            Note: the stack cannot be empty!
        Post-condition:
            None
        Return:
            the value at the top of the stack
        """
        assert not self.is_empty(), 'peeked into an empty stack'

        first_node = self.__top
        result = first_node.get_data()
        return result