#!/usr/bin/env python
#  *-* coding: cp850 *-*

import numpy as np

from .misc import matrixApply


def cooPIL2NIST( data, height, res ):
    try:
        return map( lambda x: cooPIL2NIST( x, height, res ), data )
    
    except:
        return matrixApply( 
            data,
            np.dot( 
                np.matrix( "1 0 0; 0 -1 0; 0 %.6f 1" % height ),
                np.matrix( "%.6f 0 0; 0 %.6f 0; 0 0 1" % ( 25.4 / res, 25.4 / res ) )
            )
        )

def cooNIST2PIL( data, height, res ):
    try:
        return map( lambda x: cooNIST2PIL( x, height, res ), data )
    
    except:
        return matrixApply( 
            data,
            np.dot( 
                np.matrix( "%.6f 0 0; 0 %.6f 0; 0 0 1" % ( res / 25.4, res / 25.4 ) ),
                np.matrix( "1 0 0; 0 -1 0; 0 %.6f 1" % height )
            )
        )
        
