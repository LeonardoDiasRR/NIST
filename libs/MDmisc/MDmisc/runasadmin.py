#!/usr/bin/python
# -*- coding: UTF-8 -*-

from __future__ import print_function

import ctypes
import sys

def run_as_admin( argv = None, debug = False ):
    # http://stackoverflow.com/questions/19672352/how-to-run-python-script-with-elevated-privilege-on-windows
    shell32 = ctypes.windll.shell32
    if argv is None and shell32.IsUserAnAdmin():
        return True

    if argv is None:
        argv = sys.argv
    if hasattr( sys, '_MEIPASS' ):
        # Support pyinstaller wrapped program.
        arguments = map( unicode, argv[1:] )
    else:
        arguments = map( unicode, argv )
    argument_line = u' '.join( arguments )
    executable = unicode( sys.executable )
    if debug:
        print( 'Command line: ', executable, argument_line )
    ret = shell32.ShellExecuteW( None, u"runas", executable, argument_line, None, 1 )
    if int( ret ) <= 32:
        return False
    return None
