#!/usr/bin/python
# -*- coding: UTF-8 -*-

from MDmisc.numbers import frexp10


def LaTeX_scientific_notation( nb, digits = 5, eng = False ):
    """
        Convert the scientific notation of python () to the 'traditionnal'
        annotation.
        
            >>> LaTeX_scientific_notation( 1.337e3 )
            '$1.33700 \\\\times 10^{+3}$'
    """
    try:
        mantisse, exp = frexp10( nb )
        sign = '+' if exp > 0 else ''
        
        if eng:
            expdiff = exp % 3
            if expdiff != 0:
                mantisse *= pow( 10, expdiff )
                exp -= expdiff
        
        return ( r"$%%.%df \times 10^{%%s%%d}$" % digits ) % ( mantisse, sign, exp )
    
    except:
        return nb
