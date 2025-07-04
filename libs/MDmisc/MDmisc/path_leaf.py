#!/usr/bin/env python

import ntpath


def path_leaf( path ):
    '''
        Lauritz V. Thaulow
        http://stackoverflow.com/questions/8384737/python-extract-file-name-from-path-no-matter-what-the-os-path-format
        
    '''
    head, tail = ntpath.split( path )
    return tail or ntpath.basename( head )
