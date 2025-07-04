#!/usr/bin/python
# -*- coding: UTF-8 -*-

import collections

class edict( dict ):
    def reverse( self ):
        d = {}
        for key, value in self.iteritems():
            if d.has_key( value ):
                if type( d[ value ] ) != list:
                    d[ value ] = [ d[ value ] ]
                    
                d[ value ].append( key )
            else:
                d[ value ] = key
            
        return d
    
    def search( self, searched ):
        for key, value in self.iteritems():
            if value == searched:
                return key
        
        else:
            return None
        
    def get_by_keys( self, lst ):
        return [ self.get( key ) for key in lst ]
    
    def get_r( self, path, split = "/" ):
        if isinstance( path, ( str, unicode ) ):
            path = path.split( split )
        
        tmp = self
        for key in path:
            if key in tmp.keys():
                tmp = tmp.get( key )
            else:
                error = "'%s' key not found" % key
                if len( path ) > 1:
                    error += " (searching for: %s)" % split.join( path )
                 
                raise KeyError( error )
          
        return tmp
