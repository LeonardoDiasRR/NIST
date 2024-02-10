#!/usr/bin/python
# -*- coding: UTF-8 -*-

def scientific_format( number, digits = 3 ):
    """
        Return the scientific notation of the number passed in parameter (float,
        int or string format as input).
        
            >>> scientific_format( 13371337, 3 )
            '1.337e+07'
    """
    return ( "%%.%de" % digits ) % float( number )  

def frexp10( x ):
    """
        Function to export the mantisse and the power of any number passed in
        argument.
        
            >>> print frexp10( -1337 )
            (-1.337, 3)
            >>> print frexp10( -1.337e3 )
            (-1.337, 3)
            >>> print frexp10( -0.1337 )
            (-1.337, -1)
            >>> print frexp10( -1.337e-1 )
            (-1.337, -1)
            >>> print frexp10( 1.337e-1 )
            (1.337, -1)
            >>> print frexp10( 0.1337 )
            (1.337, -1)
            >>> print frexp10( 1.337e3 )
            (1.337, 3)
            >>> print frexp10( 1337 )
            (1.337, 3)
    """
    m, e = ( "%e" % float( x ) ).split( 'e' )
    return float( m ), int( e )
