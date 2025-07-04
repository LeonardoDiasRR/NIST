#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

from .elist import flatten

class multiDirGet():
    def __init__( self, dirs = None ):
        self.dirs = []

        if type( dirs ) == list:
            map( self.addFolder, dirs )

        elif type( dirs ) == str:
            self.addFolder( dirs )
        
        self.listdirs = []
        
    def addFolder( self, f ):
        if os.path.isdir( f ):
            self.dirs.append( f )

    def get_file( self, g ):
        for d in self.dirs:
            if os.path.isfile( d + "/" + g ):
                return d + "/" + g

        else:
            raise IOError

    def get_dir( self, g ):
        for d in self.dirs:
            if os.path.isdir( d + "/" + g ):
                return d + "/" + g

        else:
            raise IOError

    def listdir( self ):
        for dir in self.dirs:
            for f in os.listdir( dir ):
                yield dir + "/" + f
                
    def preload( self ):
        for dir in self.dirs:
            self.listdirs.append( os.listdir( dir ) )
    
    def get_from_cache( self, name ):
        for i, lst in enumerate( self.listdirs ):
            if name in lst:
                return self.dirs[ i ]
        
        else:
            return None
