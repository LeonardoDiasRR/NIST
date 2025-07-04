#!/usr/bin/env python
#  *-* coding: utf-8 *-*

import struct

from .multimap import multimap
from .string import join, stringIterator

def sideways_sum( x ):
    """
        Return the sideways_sum of a number.
        
        >>> sideways_sum( 11101 )
        4
        >>> sideways_sum( 1337 )
        14
    """
    return sum( [ int( c ) for c in str( x ) ] )

def int_to_bin( x, digits = 0 ):
    """
        Return the binary value, zfilled at 'digits' caracter.
        
        >>> int_to_bin( 1337 )
        '10100111001'
        
        >>> int_to_bin( 1337, 32 )
        '00000000000000000000010100111001'
    """

    oct2bin = [ '000', '001', '010', '011', '100', '101', '110', '111' ] 
    binstring = [ oct2bin[int( n )] for n in oct( x ) ]
    binstring = ''.join( binstring ).lstrip( '0' )
    
    if digits == 'up':
        digits = 8 * ( len( binstring ) / 8 + 1 )
        
    return binstring.zfill( digits ) 

def bin_to_int( x ):
    """
        Return the int value of a binary string passed in parameter
        
        >>> bin_to_int( '00000000000000000000010100111001' )
        1337
    """
    return int( x, 2 )

def float_to_bin( f ):
    """
        convert float to binary string
        
        >>> float_to_bin( 13.37 )
        '0100000000101010101111010111000010100011110101110000101000111101'
    """
    ba = struct.pack( '>d', f )
    s = ''.join( '{:08b}'.format( ord( b ) ) for b in ba )
    return s

def bin_to_float( b ):
    """
        convert binary string to float
        
        >>> bin_to_float( '0100000000101010101111010111000010100011110101110000101000111101' )
        13.37
    """
    bf = int_to_bytes( int( b, 2 ), 8 )
    return struct.unpack( '>d', bf )[ 0 ]

def int_to_bytes( n, minlen = 0 ):
    nbits = n.bit_length() + ( 1 if n < 0 else 0 )
    nbytes = ( nbits + 7 ) / 8
    bytes = []
    
    for i in range( nbytes ):
        bytes.append( chr( n & 0xff ) )
        n >>= 8
    
    if minlen > 0 and len( bytes ) < minlen:
        bytes.extend( ( minlen - len( bytes ) ) * '0' )
    bytes.reverse()
    
    return ''.join( bytes )

def binstring_to_int( data ):
    """
        Convert string of character from binary to int
        
        >>> binstring_to_int( 'leet' )
        1818584436
    """
    b = []
    for c in data:
        b.append( int_to_bin( ord( c ), 8 ) )
    
    return bin_to_int( join( b ) )

def int_to_binstring( data, digits = 'up' ):
    """
        Convert an int to a string of character
        
        >>> int_to_binstring( 1818584436 )
        'leet'
    """
    b = int_to_bin( data, digits )
    nbites = len( b ) / 8
    
    iterbyte = stringIterator( b )
    
    return join( [ chr( bin_to_int( iterbyte.take( 8 ) ) ) for _ in xrange( nbites ) ] )

def string_to_hex( value ):
    return join( multimap( [ ord, myhex ], value ) )

def myhex( h ):
    """
        Return an hex value formatted.
        
        >>> myhex( 255 )
        'FF'
    """
    return '{:02X}'.format( h )

def hex_to_int( x ):
    return int( x, 16 )

def bindump( data ):
    ret = [ "Offset    00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F    ASCII", "-" * 77 ]
    
    for offset in xrange( 0, len( data ), 16 ):
        tmpbin = []
        tmpascii = []
        for col in xrange( 0, 16 ):
            try:
                c = data[ offset + col ]
                tmpbin.append( myhex( ord( c ) ) )
                if ord( c ) <= 31:
                    tmpascii.append( "." )
                else:
                    tmpascii.append( c )
            except:
                break
        
        bindata = " ".join( tmpbin )
        asciidata = "".join( tmpascii )
        
        line = "%06X    %-50s %s" % ( offset, bindata, asciidata )
        
        ret.append( line )
    
    return "\n".join( ret )

if __name__ == "__main__":
    import doctest
    doctest.testmod()
