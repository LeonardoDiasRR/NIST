#!/usr/bin/env python

from textwrap import wrap

def boxer( doc, comp = None ):
    if comp != None:
        ret = "\n#        "
        
        doc += ret * 2
        doc += "\n".join( wrap( comp, 65 ) ).replace( "\n", ret )
    
    return """
############################################################################
#
#    %s
#
############################################################################
    """ % doc
    