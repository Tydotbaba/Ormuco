# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 05:40:20 2019

@author: Temitayo

Description:
    This is a test module.
    It tests the LeastRecentlyUsed module
"""

import unittest
import time
from LeastRecentlyUsed import LeastRecentlyUsed


class TestCatche(unittest.TestCase):
    def setUp(self):
        # Setup an empty LeastRecentlyUsed
        self.empty = LeastRecentlyUsed(1)

        # Setup a LeastRecentlyUsed with one element
        self.one = LeastRecentlyUsed(10)
        self.one.set('a', 'test_init_one', 10)

        # Setup a LeastRecentlyUsed with more than one element
        self.many = LeastRecentlyUsed(3)
        self.many.set('a', 'test_many_init_a', 4)
        self.many.set('b', 'test_many_init_b', 10)
        self.many.set('c', 'test_many_init_c', 10)


    def test_main(self):
        # test a populated
        self.assertEqual(self.one.get('a'), 'test_init_one', 'Should be test_init_one')

        # test set overwrite
        self.one.set('a', 'test_one_overwrite', 10)        
        self.assertEqual(self.one.get('a'), 'test_one_overwrite')
        print(self.one)

        # test set overwrite new key
        self.one.set('b', 'test_one_new_key_evict', 10)
        self.assertEqual(self.one.get('b'), 'test_one_new_key_evict')

        # test a, b, c populated
        self.assertEqual(self.many.get('b'), 'test_many_init_b')
        self.assertEqual(self.many.get('a'), 'test_many_init_a')
        self.assertEqual(self.many.get('c'), 'test_many_init_c')

        # test eviction order
        self.many.set('d', 'test_eviction_order', 10)
        self.assertEqual(self.many.get('b'), None) # Should be gone
        self.assertEqual(self.many.get('d'), 'test_eviction_order')
        self.assertEqual(self.many.get('a'), 'test_many_init_a')
        self.assertEqual(self.many.get('c'), 'test_many_init_c')
        
        #test expired items in the cache
        self.many.expireItemsInCache()
        print(self.many)
        time.sleep(5)
        self.many.expireItemsInCache()
        print(self.many)


if __name__ == '__main__':
    unittest.main()