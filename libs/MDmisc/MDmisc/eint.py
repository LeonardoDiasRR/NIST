#!/usr/bin/python
# -*- coding: UTF-8 -*-

from .elist import ifany

def str_int_cmp( a, b ):
    """
        Compare the value int( a ) and int( b ) or map( int, b ).
    """
    if hasattr( b, '__iter__' ):
        return any( [ str_int_cmp( a, c ) for c in b ] )
    
    else:
        try:
            return int( a ) == int( b )
        
        except:
            return False
