#!/usr/bin/python
# -*- coding: UTF-8 -*-

from subprocess import Popen, PIPE, call

class CalledProcessError( Exception ):
    def __init__( self, returncode, cmd, output = None, expectedReturnCode = 0 ):
        self.returncode = returncode
        self.expectedReturnCode = expectedReturnCode
        self.cmd = cmd
        self.output = output
    
    def __str__( self ):
        return "Command '%s' returned %d, expected %d" % ( self.cmd, self.returncode, self.expectedReturnCode )

def check_call(*popenargs, **kwargs):
    retcode = call(*popenargs, **kwargs)
    if retcode:
        cmd = kwargs.get("args")
        if cmd is None:
            cmd = popenargs[0]
        raise CalledProcessError(retcode, cmd)
    return 0

def check_output( *popenargs, **kwargs ):
    if 'stdout' in kwargs:
        raise ValueError('stdout argument not allowed, it will be overridden.')
    
    expectedReturnCode = kwargs.pop( "expectedReturnCode", 0 )
    
    process = Popen( stdout = PIPE, *popenargs, **kwargs )
    output, unused_err = process.communicate()
    retcode = process.poll()
    
    if retcode != expectedReturnCode:
        cmd = kwargs.get( "args" )
        
        if cmd is None:
            cmd = popenargs[ 0 ]
        
        raise CalledProcessError( retcode, cmd, output = output, expectedReturnCode = expectedReturnCode )
    
    return output
