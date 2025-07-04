#!/usr/bin/env python
#  *-* coding: utf-8 *-*

import logging

from MDmisc.boxer import boxer


class MyLogger:
    def __init__( self, name = "Logger" ):
        self.mode = logging.CRITICAL
        self.format = "%(name)s -- %(levelname)s -- %(message)s"
        
        logging.basicConfig( level = self.mode, format = self.format )
        self.log = logging.getLogger( name )
    
    def setMode( self, mode ):
        mode = mode.lower()
        
        modes = {
            "debug":    logging.DEBUG,
            "info":     logging.INFO,
            "warning":  logging.WARNING,
            "error":    logging.ERROR,
            "critical": logging.CRITICAL
        }
        
        try:
            self.mode = modes[ mode ]
            self.log.setLevel( self.mode )
        except KeyError:
            self.mode = modes[ 'debug' ]
            self.log.setLevel( self.mode )
            self.warning( boxer( "logging mode level unknown : %s" % mode, "logging mode set to default ('debug')." ) )
            
    def leveler( self, msg, level ):
        return "\t" * level + msg
    
    def debug( self, msg, level = 0 ):
        msg = self.leveler( msg, level )
        self.log.debug( msg )
    
    def info( self, msg, level = 0 ):
        msg = self.leveler( msg, level )
        self.log.info( msg )
    
    def warning( self, msg, level = 0 ):
        msg = self.leveler( msg, level )
        self.log.warning( msg )
        
    def error( self, msg, level = 0 ):
        msg = self.leveler( msg, level )
        self.log.error( msg )
    
    def critical( self, msg, level = 0 ):
        msg = self.leveler( msg, level )
        self.log.critical( msg )
    
debug = MyLogger()
