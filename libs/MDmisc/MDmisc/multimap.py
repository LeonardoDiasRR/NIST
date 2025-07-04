#!/usr/bin/env python
#  *-* coding: utf-8 *-*

def multimap( funcs, value ):
    """
        Apply all functions in the 'funcs' list, in order, on the 'value' parameter.
    
    >>> f = lambda x: x.lower()
    >>> multimap( [ chr, f ], xrange( 65, 91 ) )
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    """
    for f in funcs:
        value = map( f, value )
    
    return value
