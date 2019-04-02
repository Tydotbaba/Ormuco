# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 02:39:25 2019

@author: Temitayo

Question: At Ormuco, we want to optimize every bits of software we write. 
          Your goal is to write a new library that can be integrated to the Ormuco stack.
          Dealing with network issues everyday, latency is our biggest problem. 
          Thus, your challenge is to write a new Geo Distributed LRU 
          (Least Recently Used) cache with time expiration.
          
Plan:    To solve the problem:
         Created a Node with three pointers to depict the data structure
         Used a Doubly linked list to store the cache items. 
         On item expiry, I created a method to remove the items that have expired. 
         The method shall be called in a thread that is running outside the library.
         
"""

from Node import Node
from DoublyLinkedList import DoublyLinkedList
from time import time
   
       

class LeastRecentlyUsed:
    """
    class LeastRecentlyUsed
    
    Description:
        This is the class that implemets the least recently used cache algorithm
        built the LRU using only Python primitives.
        
    @Params:
            max_size, the size of the cache.
    """
    def __init__(self, max_size):
        """
        Initialise the class.
        @Params:
            max_size, the size of the cache.
        """
        # Bare minimum checks
        assert max_size > 0, 'max_size must be greater than zero (0)'
        self._max_size = max_size
        
        # Hash here for fast key lookup and removal
        self._lookup = {}
        self._data = DoublyLinkedList()
        
    
    def expireItemsInCache( self ):
        """
        This method needs to be spawend in a thread.
        
        description:
            This is the function that  removes expired cached items from the cache.
            This function shall be called in a thread runing in a 
            module using this library
        """
        
        for cacheItem in list(self._lookup.keys()):
            #print(cacheItem, self._lookup[cacheItem].elapsedTime)
            statTime = self._lookup[cacheItem].startTime
            elapsedTime = self._lookup[cacheItem].elapsedTime
            if (time() - statTime) > elapsedTime:
                 node_to_be_removed = self._lookup[cacheItem]
                 
                 # Remove the key from the _lookup
                 del self._lookup[cacheItem]
                 
                 # Remove the node from _data
                 self._data.remove(node_to_be_removed)
  
    def set(self, key, value, elapsedTime=5):
        if key in self._lookup: 
            # Overwrite the key's value and elapsedTime
            current_node = self._lookup[key]
            current_node.value = value
            current_node.elapsedTime = elapsedTime

            # Mark as recently used by moving to the beginning of the list
            # 1) Remove the node from the DLL
            self._data.remove(current_node)

            # 2) Add the node back to the DLL
            self._data.append(current_node)
        else:
            # Otherwise create new node and append
            new_node = Node(key, value, elapsedTime)
            self._lookup[key] = new_node
            self._data.append(new_node)

        # If more than max capacity
        if len(self._lookup) > self._max_size:
            # Evict the last recently used
            # Pop the last element
            stale_node = self._data.pop()
            
            # Remove the key from the _lookup
            del self._lookup[stale_node.key]


    def get(self, key):
        # If key does not exist, don't do anything
        if key not in self._lookup: return 

        # Key exist, need to refresh to be recently used
        current_node = self._lookup[key]
        self._data.remove(current_node)
        self._data.append(current_node)
        return current_node.value


    def __repr__(self):
        return self._data.__repr__()