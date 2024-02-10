#!/usr/bin/env python

from inspect import isfunction
import functools
import warnings

from MDmisc.boxer import boxer


def deprecated( func = None, msg = None, *args ):
    if isfunction( func ):
        warnmsg = boxer( "Call to deprecated function %s" % func.__name__, msg )
        
        @functools.wraps( func )
        def f( *args, **kwargs ):
            warnings.simplefilter( 'always', DeprecationWarning )
            warnings.warn( warnmsg, category = DeprecationWarning, stacklevel = 2 )
            warnings.simplefilter( 'default', DeprecationWarning )
            
            return func( *args, **kwargs )
        
        return f
    else:
        if type( func ) == str:
            try:
                msg = " ".join( ( func, msg, ) + args ) 
            except:
                msg = func
        elif type( func ) == list:
            msg = " ".join( func )
        else:
            msg = msg

        return functools.partial( deprecated, msg = msg )
