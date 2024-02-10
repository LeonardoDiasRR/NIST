#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import functools

def memorize( f ):
    # http://codereview.stackexchange.com/questions/44039/recursive-function-high-performance-critical/44130
    cache = {}
    
    @functools.wraps( f )
    def memf( *x ):
        if x not in cache:
            cache[x] = f( *x )
            
        return cache[x]
    
    return memf
