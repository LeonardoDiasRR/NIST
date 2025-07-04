#!/usr/bin/env python

def argsort( seq ):
    # http://stackoverflow.com/questions/3382352/equivalent-of-numpy-argsort-in-basic-python/3382369#3382369
    # by unutbu
    return sorted( range( len( seq ) ), key = seq.__getitem__ )

def getByIndexes( lst, keys ):
    return [ lst[i] for i in keys ]
