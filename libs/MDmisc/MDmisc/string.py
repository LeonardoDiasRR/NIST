#!/usr/bin/python
# -*- coding: UTF-8 -*-

import collections
import unicodedata

def upper( data ):
    """
        Function equivalent of the str.upper() function.
    """
    return data.upper()

def join( c, i = None ):
    """
        Function equivalent of the str.join() function. If the function is
        called only with one argument, i.e. the list, the join is made without
        spacing between the elements of the list.
        
            >>> join( ";", ['1-2-3', '4-5-6', '7-8-9'] )
            '1-2-3;4-5-6;7-8-9'
            
            >>> join( ['1', '2', '3', '4', '5', '6'] )
            '123456'
    """
    if i == None:
        c, i = "", c
    
    try:
        return c.join( i )
    
    except TypeError:
        return c.join( map( str, i ) )

def join_r( c, lst = None ):
    """
        Recursive join a list of list.
        
            >>> join_r( [ "", "-", ";" ], [[['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']], [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]] )
            '123-456-789;123-456-789'
            
            >>> join_r( "-", [[['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']], [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]] )
            '1-2-3-4-5-6-7-8-9-1-2-3-4-5-6-7-8-9'
            
            >>> join_r( [[['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']], [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]] )
            '123456789123456789'
            
            >>> join_r( "-", [] )
        
    """
    if lst == None:
        c, lst = [], c
    
    if lst == [] or lst == ():
        return
    
    if isinstance( c, ( list, tuple ) ):
        if isinstance( lst[ 0 ], ( list, tuple ) ):
            lst = map( lambda x: join_r( c[ :-1 ], x ), lst )
        
        try:
            last = c[ -1 ]
        except:
            last = ""
        
    elif isinstance( c, str ):
        if isinstance( lst[ 0 ], list ):
            lst = map( lambda x: join_r( c, x ), lst )
            
        last = c
        
    return join( last, lst )

def split( i, c ):
    """
        Function equivalent of str.split()
        
            >>> split( ";", "1-2-3;4-5-6;7-8-9" )
            ['1-2-3', '4-5-6', '7-8-9']
    """
    return c.split( i )

def split_r( lst, s ):
    """
        Recursive split a string.
        
            >>> split_r( [ ';', '-' ], "1-2-3;4-5-6;7-8-9" )
            [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    """
    try:
        return map( lambda x: split_r( lst[ 1: ], x ), s.split( lst[ 0 ] ) )
    except:
        return s

class stringIterator( object ):
    def __init__( self, data ):
        self.data = data
        self.index = 0
        self.len = len( data )
        self.toend = self.len
        
    def next( self ):
        ret = self.data[ self.index ]
        self.index += 1
        self.toend -= 1
        return ret
    
    def take( self, n ):
        ret = ''.join( self.data[ self.index: self.index + n ] )
        self.index += n
        self.toend -= n
        return ret
    
    def show( self, n = 1 ):
        return ''.join( self.data[ self.index: self.index + n ] )
    
    def __iter__( self ):
        return self
    
def split_no_empty( data, string ):
    """
        Return the data.split( string ) list without the empty values.
        
            >>> split_no_empty( "1-2-3--4-5", "-" )
            ['1', '2', '3', '4', '5']
    """
    return [ value for value in data.split( string ) if value != "" ]

def unicode2str( data ):
    if type( data ) == str:
        return data
     
    elif type( data ) == unicode:
        return str( data.encode( 'utf-8', 'ignore' ).strip() )
    
    elif isinstance( data, collections.Mapping ):
        return dict( map( unicode2str, data.iteritems() ) )
    
    elif isinstance( data, collections.Iterable ):
        return type( data )( map( unicode2str, data ) )
    
    else:
        return data

def remove_accents( data, encodingin = 'ISO-8859-1', encodingout = 'ASCII' ):
    if isinstance( data, dict ):
        for key, value in data.iteritems():
            try:
                data[ key ] = remove_accents( value, encodingin, encodingout )
            except TypeError:
                continue
        return data
    else:
        if isinstance( data, str ):
            data = unicode( data, encodingin )
        
        return unicodedata.normalize( 'NFKD', data ).encode( encodingout, 'ignore' )
