# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 10:20:13 2019

@author: Temitayo

Description:
    This is a test module.
    It tests the version library
"""

import unittest
from version import processVersion


class TestVersion(unittest.TestCase):
    def testProcessVersion(self):
        # Setup an empty LeastRecentlyUsed
        self.assertEqual(processVersion(["1.2", "1.1"]), 
                         "version 1.2 is greater than 1.1.")
            
        self.assertEqual(processVersion(["1", "1.1"]), None)
        
        self.assertEqual(processVersion(["2.0.2", "1.1"]), None)
        
        self.assertEqual(processVersion(["1.2.0", "0.1.1"]), 
                         "version 1.2.0 is greater than 0.1.1.")

        self.assertEqual(processVersion(["the", "0.1.1"]), None)
    #def test_main(self):
       


if __name__ == '__main__':
    unittest.main()