#!/usr/bin/python
# -*- coding: UTF-8 -*-

class rotating_list( object ):
    def __init__( self, data = None ):
        if data == None:
            self.data = []
        else:
            self.data = data
        self.i = 0
        self.meta = []
    
    def meta_append( self, el ):
        self.meta.append( el )
    
    def meta_isin( self, el ):
        return el in self.meta
    
    def meta_get_index( self, el ):
        try:
            return self.meta.index( el )
        except ValueError:
            return None
    
    def current( self ):
        return self.data[ self.i ]
    
    def last( self ):
        return self.data[ -1 ]
    
    def append( self, el ):
        return self.data.append( el )
    
    def get_list( self ):
        return self.data
    
    def next( self ):
        d = self.data[ self.i ]
        self.i = ( self.i + 1 ) % len( self.data )
        return d
    
    def rnext( self ):
        n = self.next()
        if isinstance( n, rotating_list ):
            return n.next()
        else:
            return n
    
    def __repr__( self, *args, **kwargs ):
        return str( self.data )
    
    def __getitem__( self, index ):
        return self.data[ index ]
    
    def __setitem__( self, index, value ):
        self.data[ index ] = value
