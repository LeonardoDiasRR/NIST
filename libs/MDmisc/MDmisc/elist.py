#!/usr/bin/python
# -*- coding: UTF-8 -*-

import collections

from .map_r import map_r

def replace_r( x, s, r ):
    def test( x, s = s, r = r ):
        if x == s:
            return r
        else:
            return x
    
    return map_r( test, x )

def flatten( lst ):
    for e in lst:
        if isinstance( e, collections.Iterable ) and not isinstance( e, basestring ):
            for sublist in flatten( e ):
                yield sublist
        else:
            yield e

def ifany( a, b ):
    for i in a:
        if i in b:
            return True
    else:
        return False

def ifall( a, b ):
    for i in a:
        if i not in b:
            return False
    
    else:
        return True

def which( a, b ):
    for e in a:
        if e in b:
            return e
    else:
        return None

def rotate( lst, x ):
    return lst[ x : ] + lst[ : x ]

class elist( list ):
    """
        Expension of the list class, adding multiples functionnalities.
    """
    def __init__( self, *data ):
        super( elist, self ).__init__( flatten( data ) )
        
    def __call__( self, *args, **kwargs ):
        """
            Call a specific function of all elements of the list, and return the
            list of results.
        """
        return [ e( *args, **kwargs ) for e in self ]

def chunks( l, n ):
    for i in xrange( 0, len( l ), n ):
        yield l[i:i + n]
