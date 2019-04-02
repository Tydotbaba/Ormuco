# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 02:40:04 2019

@author: Temitayo
"""

from time import time

class Node:
    """
    Node with three pointers.
    @params: 
        key, value, elapsedTime
    """
    def __init__(self, key, value, elapsedTime = 10, next=None, prev=None):
        self.key = key
        self.value = value
        self.startTime = time()
        self.elapsedTime = elapsedTime
        self.next = self.prev = None
        return

    def __repr__(self):
        """
        Return the string representation of the list.
        """
        str_format = '{}'
        data_str = ''
        if self.key:
            data_str += '[{}, {}, {}]'.format(self.key, self.value, self.elapsedTime)
        return str_format.format(data_str)

    def has_value(self, key):
        """
        method to compare the key with the node key
        """
        if self.key == key:
            return True
        else:
            return False