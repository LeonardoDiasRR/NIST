#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import division

import numpy as np

from scipy.spatial import Delaunay
from scipy.spatial import ConvexHull

from MDmisc.elist import rotate, flatten

################################################################################
# 
################################################################################

def medianXY( data ):
    x, y = zip( *data )
    return np.median( x ), np.median( y )

def meanXY( data ):
    x, y = zip( *data )
    return np.mean( x ), np.mean( y )

def minmaxXY( data ):
    return map( lambda a: ( max( a ) + min( a ) ) / 2, zip( *data ) )

################################################################################
#    Matrix manipulation
################################################################################

def matrixApply( point, matrix ):
    inputx, inputy = point
    return np.dot( np.matrix( "%f %f 1" % ( inputx, inputy ) ), np.matrix( matrix ) ).ravel().tolist()[0][0:2]

def matrixListApply( list, matrix ):
    ret = []

    for p in list:
        ret.append( matrixApply( p, matrix ) )

    return ret

def matrixMatrixApply( a, b ):
    ret = []
    for p in a.tolist():
        ret.append( matrixApply( p, b ) )
    
    return np.matrix( ret )

def multiDot( *argv ):
    ret = argv[0]
    
    for m in argv[1:]:
        ret = np.dot( 
            ret,
            m
        )
    
    return ret

def rotMatrix( theta, degree = True ):
    if degree:
        theta = theta / 180 * np.pi
    
    c = np.cos( theta )
    s = np.sin( theta )
    
    return np.array( [[ c, -s, 0 ], [ s, c, 0 ], [ 0, 0, 1 ] ] ).T

def dxdyMatrix( dx, dy ):
    return np.array( [[ 1, 0, 0 ], [ 0, 1, 0 ], [ dx, dy, 1 ] ] ).T

################################################################################
#    List manipulation
################################################################################

def shift_point( point, delta, revert = False ):
    point = list( point )
    r = -1 if revert else 1
    
    for i in xrange( len( delta ) ):
        point[ i ] += r * delta[ i ]
    
    return point

def shift_list( points, delta, revert = False ):
    return [ shift_point( p, delta, revert ) for p in points ]

################################################################################
#    Hull related functions
################################################################################

def in_hull( p, hull ):
    if not isinstance( hull, Delaunay ):
        hull = Delaunay( hull )

    return hull.find_simplex( p ) >= 0

def points_area( points ):
    points = np.asarray( points )
    hull = ConvexHull( points )
    contour = list( flatten( hull.vertices ) )
    corners = points[ contour, ].tolist()
    return polygon_area( corners )

def points_density( points ):
    area = points_area( points )
    return len( points ) / area
    
def polygon_area( corners ):
    area = 0
    x, y = zip( *corners )
    for x, y1, y2 in zip( x, rotate( y, 1 ), rotate( y, -1 ) ):
        area += x * ( y1 - y2 )
    
    return 0.5 * abs( area )
