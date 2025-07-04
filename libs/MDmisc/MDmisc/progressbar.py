#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#      Corey Goldberg - 2010
#      ascii command-line progress bar with percentage and elapsed time display
#
#      http://code.google.com/p/corey-projects/source/browse/trunk/python2/progress_bar.py
#
# Semble ne fonctionner qu'avec une version 2.x de python.

import sys
import math
import time

class ProgressBar:
    def __init__( self, max = 100 ):
        self.inittime = time.time()
        self.remaintime = 0
        self.max = max
        self.actual = 0
        self.prog_bar = '[]'
        self.fill_char = '#'
        self.wc = "/-\\|"
        self.nbupdate = 0
        self.width = 35
        self.__update_amount( 0 )
    
    def clean( self ):
#        if sys.platform.lower().startswith('win'):
            print self, "\r",
#        else:
#            print self, chr(27) + '[A'
        
    def update( self, n = None ):
        if n == None:
            n = self.actual
        else:
            self.actual = n
        
        self.nbupdate += 1
        
        remain = ""
        
        if self.nbupdate % 100:
            diff = time.time() - self.inittime
            self.remaintime = self.max * diff / n - diff
    
        if self.remaintime < 60:
            remain = "%02d sec" % self.remaintime
        elif self.remaintime < 3600:
            remain = "%02d min %02d sec" % ( self.remaintime / 60, self.remaintime % 60 )
        else:
            heure = self.remaintime / 3600.0
            min = ( self.remaintime - math.floor( heure ) * 3600 ) / 60.0
            sec = ( self.remaintime - math.floor( heure ) * 3600 - math.floor( min ) * 60 )
            remain = "%02d h %02d min %02d sec" % ( heure, min, sec )
        
        remain = "%18s" % remain
            
        self.__update_amount( ( n / float( self.max ) ) * 100.0 )
        self.prog_bar += '  %d / %s  (%6.2f %s ~ %s)' % ( n, self.max, 100 * float( n ) / float( self.max ), "%", remain )
        
        self.clean()
        
    def __update_amount( self, new_amount ):
        percent_done = int( round( ( new_amount / 100.0 ) * 100.0 ) )
        all_full = self.width - 2
        num_hashes = int( round( ( percent_done / 100.0 ) * all_full ) )
        self.prog_bar = '[' + self.fill_char * num_hashes + self.wc[self.nbupdate % 4] + ' ' * ( all_full - num_hashes ) + ']'
        
    def __str__( self ):
        return str( self.prog_bar )

def pb( a, b, s ):
    fill_char = '#'
    
    percent_done = int( round( ( a / 100.0 ) * 100.0 ) )
    all_full = s - 2
    num_hashes = int( round( ( percent_done / 100.0 ) * all_full ) )
    prog_bar = '[' + fill_char * num_hashes + ' ' * ( all_full - num_hashes ) + ']  ' + "%s / %s (%.2f%s)" % ( a, b, float( a ) / float( b ) * 100, '%' )
    
    return prog_bar
