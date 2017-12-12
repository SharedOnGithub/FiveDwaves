'''
Created on Nov 29, 2017

@author: luke
'''

from __future__ import print_function


def ispalindrome(word_combination):
    # print(word)
    if len(word_combination) > 0 :
        t = ''.join(word_combination).lower()        # Palindrome test should be case-insensitive and not empty
        return t[::-1] == t
    else:
        return False

class wordgame(object):
    '''
    A game to generate combinations from given word list
    '''
    words = None


    def __init__(self, params):
        '''
        Constructor
        
        @params a list of word to play the game with
        '''
        self.words = params
        if self.words is None or len(self.words) == 0:
            raise ValueError("word list is not provided or empty")
        
    def combinations(self):
        '''
        Generate all combinations from given word list, going from length 1 to full length of the word list
        '''
        from itertools import chain, combinations
        return chain(*map(lambda x: combinations(self.words, x), range(1, len(self.words) + 1)))
        
if __name__ == "__main__":
    game = wordgame(['Gimli', 'Fili',  'Ilif',  'Ilmig', 'Mark'])
    print([word for word in game.combinations() if ispalindrome(word)])