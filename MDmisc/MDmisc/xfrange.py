#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def xfrange( start, stop = None, step = 1.0 ):
    """
        Generator function for float xrange()
        
        >>> [ x for x in xfrange( 0, 1, 0.12 ) ]
        [0.0, 0.12, 0.24, 0.36, 0.48, 0.6, 0.72, 0.84, 0.96]
    """
    if stop is None:
        stop = float( start )
        start = 0.0

    cur = float( start )

    while cur <= stop:
        yield cur
        cur += step
