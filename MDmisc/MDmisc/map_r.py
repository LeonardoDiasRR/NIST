#!/usr/bin/env python
#  *-* coding: utf-8 *-*

def map_r( fun, data ):
    if hasattr( data, "__iter__" ):
        return [ map_r( fun, e ) for e in data ]
    else:
        return fun( data )
