#!/usr/bin/env python
#  *-* coding: cp850 *-*

from PIL import Image

def codeImage( data, image, size, limit = 250 ):
    im = Image.open( image )
    im = im.resize( size, Image.BILINEAR )
    im = im.convert( "L" )
     
    str = ""
    
    try:
        i = 0
        for y in xrange( 0, im.size[1] ):
            for x in xrange( 0, im.size[0] ):
                val = im.getpixel( ( x, y ) )
                if val > limit:
                    str += " "
                
                else:
                    str += data[i]
            
                    i += 1
            str += "\n"
        
        str += "\n\n"
    except:
        pass
        
    j = 0
    while True:
        if j % size[0] == 0:
            str += "\n"
        j += 1
        
        try:
            str += "%s" % data[ i ]
            i += 1
        except:
            break

    return str
