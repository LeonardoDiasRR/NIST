#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import print_function

import zipfile
from cStringIO import StringIO as io

class ZipFileExtended( zipfile.ZipFile ):
    def removeFile( self, *filenames ):
        outbuff = io()
        
        try:
            with zipfile.ZipFile( self.fp, 'r' ) as zipread:
                with zipfile.ZipFile( outbuff, 'w' ) as zipwrite:
                    for item in zipread.infolist():
                        if item.filename not in filenames:
                            data = zipread.read( item.filename )
                            zipwrite.writestr( item, data )
            
            self.fp = outbuff
            
            self.filelist = []
            self._RealGetContents()
            
        except Exception as e:
            print( str( e ) )
            
        finally:
            return
            
    def saveToFile( self, outputfile = None ):
        if outputfile == None:
            outputfile = self.filename
        
        with open( outputfile, "wb+" ) as fp:
            fp.write( self.fp.getvalue() )
    