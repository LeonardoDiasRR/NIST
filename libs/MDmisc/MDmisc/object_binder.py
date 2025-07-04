#!/usr/bin/python
# -*- coding: UTF-8 -*-

from .eobject import eobject
from .elist import elist, flatten

################################################################################

class object_binder( eobject ):
    def __init__( self, *_data ):
        self._data = flatten( _data )
        
    def __getattr__( self, name, *args, **kwargs ):
        return elist( [ getattr( d, name ) for d in self._data ] )
    
    def __iter__( self ):
        for a in self._data:
            yield a
    