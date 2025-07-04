#!/usr/bin/python
# -*- coding: UTF-8 -*-

import base64
from cStringIO import StringIO
import gzip
import pickle


def objectToPickle( obj ):
    fp = StringIO()
    pickle.dump( obj, fp )
    
    return fp.getvalue()

def pickleToObject( p ):
    fp = StringIO()
    fp.write( p )
    fp.seek( 0 )
    
    return pickle.load( fp )

def compress( obj ):
    zip_text_file = StringIO()
      
    zipper = gzip.GzipFile( mode = 'wb', fileobj = zip_text_file )
      
    zipper.write( obj )
    zipper.close()
      
    return base64.b64encode( zip_text_file.getvalue() )

def decompress( data ):
    sample_text_file = gzip.GzipFile( mode = 'rb', fileobj = StringIO( base64.b64decode( data ) ) )
    ret = sample_text_file.read()
    sample_text_file.close()
    
    return ret

def objectToCompressed( obj ):
    return compress( objectToPickle( obj ) )

def compressedToObject( data ):
    return pickleToObject( decompress( data ) )

def decompressPickleFromFile( f ):
    with open( f ) as fp:
        return compressedToObject( fp.read() )
