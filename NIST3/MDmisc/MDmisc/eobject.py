#!/usr/bin/python
# -*- coding: UTF-8 -*-

class eobject( object ):
    def apply_to_all( self, func, lst, *args, **kwargs ):
        for obj in lst:
            getattr( obj, func )( *args, **kwargs )
