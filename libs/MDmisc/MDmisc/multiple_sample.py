#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random

class multiple_sample( object ):
    """
        Get a random sample of 'size' from the range between 0 and 'maxValue'.
        
            >>> import random
            >>> random.seed( 1337 )
        
        Get 5 samples of 3 elements between 0 and 10: 
        
            >>> print [ i for i in multiple_sample( 3, 10, 5 ) ]
            [[6, 4, 2], [5, 1, 6], [3, 7, 8], [3, 8, 1], [6, 8, 0]]
    """
    def __init__( self, size, maxValue, number = None ):
        self.size = size
        self.maxValue = maxValue
        self.number = number
        
        self.lst = xrange( self.maxValue )
        self.i = 0
        
    def __iter__( self ):
        return self

    def __next__( self ):
        return self.next()

    def next( self ):
        if self.number != None and self.i >= self.number:
            raise StopIteration()
        else:
            self.i += 1
            return random.sample( self.lst, self.size )
    
    def __call__( self ):
        return self.next()
    
