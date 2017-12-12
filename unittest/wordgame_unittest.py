'''
Created on Nov 29, 2017

@author: luke
'''
from __future__ import print_function

import unittest
from math import factorial
from wordgame import ispalindrome
from wordgame import wordgame


class wordgame_unittest(unittest.TestCase):


#     def setUp(self):
#         pass
# 
# 
#     def tearDown(self):
#         pass


    def test_ispalindrome(self):
        self.assertTrue(ispalindrome('radar'))
        self.assertTrue(ispalindrome('Aba'))
        self.assertTrue(ispalindrome(['A', 'b', 'a']))
        self.assertTrue(ispalindrome(['Aa', 'bb', 'aa']))
        
    def test_combinations(self):
        data = ['a', 'b', 'c']
        answer = [('a',), ('b',), ('c',), ('a', 'b'), ('a', 'c'), ('b', 'c'), ('a', 'b', 'c')]
        game = wordgame(data)
        c = list(game.combinations())
        self.assertEqual(len(c), len(list(set(c))), 'combinations are not unique')
        self.assertEqual(set(answer), set(c), 'combinations does\'t match known answer')
        
   
    def test_combinations2(self):
        data = ['a', 'b', 'c', 'd', 'e', 'f']
        t = len(data)
        game = wordgame(data)
        c = list(game.combinations())
        for x in xrange(1, len(data)):
            cx = [e for e in c if len(e) == x]
            self.assertEqual(len(cx), len(list(set(cx))), 'combinations are not unique')
            self.assertEqual(len(cx), factorial(t) / (factorial(x)*factorial(t-x)), 'combinations count is wrong')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'wordgame_unittest.testName']
    unittest.main()