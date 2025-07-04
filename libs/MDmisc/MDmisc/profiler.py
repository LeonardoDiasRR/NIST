################################################################################
#    Profiler
################################################################################

from __future__ import print_function

import functools 
import time


try:
    profile
except:
    class profile( object ):
        def __init__( self, func ):
            self.func = func
            functools.update_wrapper( self, func )
            
        def __call__( self, *args, **kwargs ):
            return self.func( *args, **kwargs )

################################################################################
#    Timer
################################################################################

class Timer:
    def __init__( self, desc = "Timing" ):
        self.desc = desc
        
    def __enter__( self ):
        self.start = time.clock()
        return self

    def __exit__( self, *args ):
        self.end = time.clock()
        self.interval = self.end - self.start
        
        print( "%-15s : %s" % ( self.desc, self.interval ) )
        