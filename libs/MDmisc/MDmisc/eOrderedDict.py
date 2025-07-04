#!/usr/bin/python
# -*- coding: UTF-8 -*-

from collections import OrderedDict

class eOrderedDict( OrderedDict ):
    def get_r( self, path, default = None, sep = "/" ):
        ret = self
        try:
            for key in path.split( sep ):
                ret = ret.get( key )
            return ret
        
        except:
            return default

def eOrderedDictParser( obj ):
    if isinstance( obj, OrderedDict ):
        obj.__class__ = eOrderedDict
        
        for i, ( k, v ) in enumerate( obj.iteritems() ):
            eOrderedDictParser( v )
    
    elif isinstance( obj, list ):
        for i, v in enumerate( obj ):
            eOrderedDictParser( v )
    
    return obj
