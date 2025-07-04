#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import warnings

class nowarnings( object ):
    def __init__( self, w ):
        self.w = w
        return
    
    def __enter__( self ):
        warnings.filterwarnings( "ignore", category = self.w )
        
    def __exit__( self, *args, **kwargs ):
        warnings.resetwarnings()
