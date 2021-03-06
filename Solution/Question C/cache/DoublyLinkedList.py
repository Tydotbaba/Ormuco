# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 02:36:56 2019

@author: Temitayo
Description:
    This is the doubly linked list implemetation
"""

from Node import Node


class DoublyLinkedList:
    """
    Simple doubly linked list implementation with simple API.
    
    """
    def __init__(self):
        self.head = self.tail = None
        self.__size = 0


    def append(self, node):
        """
        Appends to the beginning of the list.
        """
        
        # Check if this is the initial insert
        if not self.head:
            self.head = self.tail = node
        else:
            #return if the node already exitsed
            if self.hasNode(node):
                return
            # Make node the new head and the old head point to the next head
            node.next = self.head
            node.prev = None
            self.head.prev = node
            self.head = node

        # Increment size
        self.__size += 1


    def hasNode(self, node):
        """
        Search the linked list to determine if the node exists
        A mechanism to check for duplicated nodes.
        """
        # define current_node
        current_node = self.head
        
        key = node.key

        
        while current_node is not None:
            if current_node.has_value(key):
                #node exists in List
                return True
            # jump to the linked node
            current_node = current_node.next
        
        #node does not exit in List
        return False
        
        
        
    def remove(self, node):
        """
        Removes and returns node from the list and appropriately joins the gap left by
        removing the node.
        """
        # Don't forget to set the head/tail properly
        if self.head == node:
            self.head = self.head.next
        if self.tail == node:
            self.tail = self.tail.prev

        # Join the gap
        next_node = node.next
        prev_node = node.prev

        # Make sure these nodes are not None
        if prev_node:
            prev_node.next = next_node
        if next_node:
            next_node.prev = prev_node

        # Free up memory
        node.next = node.prev = None

        # Decrement size
        self.__size -= 1
        return node


    def pop(self):
        """
        Returns the last node from the list.
        """
        tail_node = self.tail
        prev_node = self.tail.prev

        # Make prev_node's next point to None
        # If the previous node of tail is None, that means it is the sole node in the list
        if prev_node:
            prev_node.next = None

        # Set tail to be first
        self.tail = prev_node

        # Decrement size
        self.__size -= 1

        # Don't forget to check potential new head
        if self.__size < 2:
            self.head = self.tail
        return tail_node


    def __len__(self):
        """
        Returns the size of the linked list.
        """
        return self.__size


    def __repr__(self):
        """
        Return the string representation of the list.
        """
        str_format = '[{}]'
        data_str = ''
        node = self.head
        while node:
            data_str += "'{}': '{}'".format(node.key, node.value)
            node = node.next
            if node: 
                data_str += ', '
        return str_format.format(data_str)


if __name__ == '__main__':
    #pass
    # Simple check
    a = DoublyLinkedList()
    x = Node('x',2)
    y = Node('y',3)
    a.append(x)
    a.append(y)
    #print(a)
    #a.remove(y)
    print(a)
    #a.pop()
    #print(len(a))
    print(a)
    a.append(y)
    a.append(x)
    print(a)