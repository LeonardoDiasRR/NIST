#!/usr/bin/env python

from __future__ import print_function

import _warnings
from tempfile import mkdtemp

import os as _os
import sys as _sys


class TemporaryDirectory( object ):
    """
        Create and return a temporary directory. This has the same behavior as
        mkdtemp but can be used as a context manager. For example:

            with TemporaryDirectory() as tmpdir:
                ...

        The os.setcwd() function is called in the TemporaryDirectory() to wet
        the working directory to the tempdir. The current working directory is
        resetted upon exiting the contex.
        
        Upon exiting the context, the directory and everything contained in it
        are removed.
        
        Original code:
            Leonardo.Z
            http://stackoverflow.com/questions/19296146/tempfile-temporarydirectory-context-manager-in-python-2-7
        
        Modified by:
            Marco De Donno (mdedonno1337@gmail.com)
    
    """

    def __init__( self, suffix = "", prefix = "tmp", dir = None ):
        self.cwd = _os.getcwd()
        
        self._closed = False
        
        try:
            self.name = mkdtemp( suffix, prefix, dir )
        except:
            self.name = None
        
    def __repr__( self ):
        return "<{} {!r}>".format( self.__class__.__name__, self.name )

    def __enter__( self ):
        _os.chdir( self.name )
        return self.name

    def cleanup( self, _warn = False ):
        if self.name and not self._closed:
            try:
                self._rmtree( self.name )
            except ( TypeError, AttributeError ) as ex:
                if "None" not in str( ex ):
                    raise
                print( "ERROR: {!r} while cleaning up {!r}".format( ex, self, ), file = _sys.stderr )
                return
            self._closed = True

    def __exit__( self, exc, value, tb ):
        self.cleanup()
        _os.chdir( self.cwd )

    def __del__( self ):
        self.cleanup( _warn = True )

    _listdir = staticmethod( _os.listdir )
    _path_join = staticmethod( _os.path.join )
    _isdir = staticmethod( _os.path.isdir )
    _islink = staticmethod( _os.path.islink )
    _remove = staticmethod( _os.remove )
    _rmdir = staticmethod( _os.rmdir )
    _warn = _warnings.warn

    def _rmtree( self, path ):
        for name in self._listdir( path ):
            fullname = self._path_join( path, name )
            try:
                isdir = self._isdir( fullname ) and not self._islink( fullname )
            except OSError:
                isdir = False
            if isdir:
                self._rmtree( fullname )
            else:
                try:
                    self._remove( fullname )
                except OSError:
                    pass
        try:
            self._rmdir( path )
        except OSError:
            pass

class TemporaryWorkIn( object ):
    """
        Context manager to work in a specific directory only in this context.
        Usefull to use os.system() function to call external software in a
        specific directory, without having to make the os.chdir() a the end...
    """
    def __init__( self, name ):
        self.cwd = _os.getcwd()
        self.name = name
    
    def __enter__( self ):
        _os.chdir( self.name )
        return self.name
    
    def __exit__( self, exc, value, tb ):
        _os.chdir( self.cwd )
